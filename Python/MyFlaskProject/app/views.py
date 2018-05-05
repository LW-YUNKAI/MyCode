import random
from datetime import datetime

from flask import render_template, flash, redirect, request, url_for, g, session, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.sql.elements import or_

from app import app, login_manager, db

# 定义路径
from app.form import PostForm
from app.models import User, Post, Gift

from app.services import *

data = {}


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
def index():
    u = g.user
    p = []
    total_post = Post.query.filter_by(disabled=False).all()
    for item in total_post:
        item_user = User.query.filter_by(id=item.user_id).first()
        p.append({
            'author': {'username': item_user.username},
            'body': item.body,
            'time': item.timestamp,
            'title': item.title
        })
    return render_template("index.html",
                           title='Home',
                           user=u,
                           posts=p)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


# ===============================================================================
# 用户登录
# ===============================================================================
@app.route('/login', methods=['GET', 'POST'])
def login():
    # validate_on_submit 函数进行了表单验证，成功返回true
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user is not None and user.verify_password(password):
            login_user(user)
            flash('Login successfully！Welcome!' + str(user.username), 'success')
            return redirect(url_for('index'))
        else:
            flash('Error！Username or password incorrect.', 'danger')
    return render_template('login.html', title='login')


# ===============================================================================
# 用户注销
# ===============================================================================
@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('You have been logout.', 'success')
    return redirect(url_for('login'))


# ===============================================================================
# 用户注册
# ===============================================================================
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['first_name'] + request.form['last_name']
        user = User.query.filter(or_(User.username == username, User.email == email)).first()
        if user is None:
            User.insert_user(username=username, password=password, email=email)
            flash('Register successfully!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Error! The username or email has already been registered.', 'danger')
    return render_template('register.html',
                           title='register')


# 发布post
@login_required
@app.route('/writepost', methods=['POST', 'GET'])
def writepost():
    user = g.user
    form = PostForm()
    title = form.title.data
    body = form.body.data
    if request.method == 'POST':
        if form.validate_on_submit():
            if body is not None and title is not None:
                Post.insert_post(user.id, title, body)
                flash('write post successfully！', 'success')
                return redirect(url_for('index'))
            else:
                flash('Error！title or body empty.', 'danger')
        return redirect(url_for('app.writepost'))
    return render_template('writepost.html',
                           title='Post',
                           form=form,
                           user=user)


# 个人页面
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User ' + username + ' not found.')
        return redirect(url_for('index'))
    p = []
    total_post = Post.query.filter_by(disabled=False).all()
    for item in total_post:
        item_user = User.query.filter_by(id=item.user_id).first()
        if item_user.id == user.id:
            p.append({
                'author': {'username': item_user.username},
                'body': item.body,
                'time': item.timestamp,
                'title': item.title,
                'id': item.id
            })

    return render_template('user.html',
                           user=user,
                           posts=p)


# 删除post
@app.route("/disable_post", methods=['GET', 'POST'])
@login_required
def disable_post():
    # title = request.args.get()
    post_id = request.args.get('id', type=int, default=0)
    print(post_id)
    # print(title)
    Post.query.filter_by(id=post_id).update({Post.disabled: True})
    db.session.commit()
    return redirect(url_for('index'))


# 抽奖
@app.route('/score2gift')
@login_required
def score2gift():
    userR = g.user
    p = []
    total_gift = Gift.query.filter_by(obtain=True).all()
    for item in total_gift:
        item_user = User.query.filter_by(id=item.user_id).first()
        p.append({
            'user': item_user.username,
            'prize': item.name,
            'time': item.time,
        })

    return render_template('score2gift.html',
                           user=userR,
                           prize=p)


# ===============================================================================
# 添加积分
# ===============================================================================
@app.route('/add_score')
@login_required
def add_score():
    score = int(request.args.get('score'))
    u = g.user
    user_id = u.id
    user_add_score(user_id, score)
    return jsonify(tip='添加成功！')


# ===============================================================================
# 抽奖转盘
# ===============================================================================
@app.route('/roll')
@login_required
def roll():
    user = g.user
    if user.score < 10:
        return jsonify(gift_code=0)
    # 减积分
    user_add_score(user.id, -10)
    tg = []
    # 获取可得到奖品的tag
    total_gift = db.session.query(Gift).filter_by(obtain=False).all()
    for item in total_gift:
        if item.tag not in tg:
            tg.append(item.tag)
    print(tg)
    if len(tg) == 4:
        user_add_score(user.id, 10)
        return jsonify(gift_code=9)
    # 抽取奖品的tag
    gift_code = random.sample(tg, 1)[0]
    print(gift_code)
    if gift_code == 1:
        # 一等奖
        gf = db.session.query(Gift).filter_by(tag=gift_code, obtain=False).first()
        print(gf.id)
        db.session.query(Gift).filter_by(id=gf.id).update(
            {Gift.user_id: user.id, Gift.obtain: True, Gift.time: datetime.now()})
        db.session.commit()
        pass
    elif gift_code == 2:
        # 二等奖
        gf = db.session.query(Gift).filter_by(tag=gift_code, obtain=False).first()
        print(gf.id)
        db.session.query(Gift).filter_by(id=gf.id).update(
            {Gift.user_id: user.id, Gift.obtain: True, Gift.time: datetime.now()})
        db.session.commit()
        pass
    elif gift_code == 3:
        # 三等奖
        gf = db.session.query(Gift).filter_by(tag=gift_code, obtain=False).first()
        print(gf.id)
        db.session.query(Gift).filter_by(id=gf.id).update(
            {Gift.user_id: user.id, Gift.obtain: True, Gift.time: datetime.now()})
        db.session.commit()
        pass
    elif gift_code == 4:
        # 四等奖
        gf = db.session.query(Gift).filter_by(tag=gift_code, obtain=False).first()
        print(gf.id)
        db.session.query(Gift).filter_by(id=gf.id).update(
            {Gift.user_id: user.id, Gift.obtain: True, Gift.time: datetime.now()})
        db.session.commit()
        pass
    elif gift_code == 5:
        # 没中奖
        pass
    elif gift_code == 6:
        # 没中奖
        pass
    elif gift_code == 7:
        # 没中奖
        pass
    elif gift_code == 8:
        # 没中奖
        pass
    # 奖品设置为已经抽中
    return jsonify(gift_code=gift_code)


# ===============================================================================
# playground
# ===============================================================================
@app.route('/playground')
def playground():
    data['user'] = g.user
    return render_template('playground.html', data=data)
