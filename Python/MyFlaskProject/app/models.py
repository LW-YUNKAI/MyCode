from datashape import unicode
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    score = db.Column(db.Integer)  # 积分

    disabled = db.Column(db.Boolean)  # 删除

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def insert_user(email, username, password):
        user = User(email=email, username=username, password=password)
        user.score = 0
        user.disabled = False
        db.session.add(user)
        db.session.commit()
        return user.id

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.String(2000))
    timestamp = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User, backref='post')

    disabled = db.Column(db.Boolean)  # 删除

    @staticmethod
    def insert_post(u_id, title, body):
        post = Post(user_id=u_id, title=title, body=body, timestamp=datetime.now())
        post.disabled = False
        db.session.add(post)
        db.session.commit()
        return post.id

    def __repr__(self):
        return '<Post %r>' % self.title


class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.Integer)  # 几等奖
    disabled = db.Column(db.Boolean)  # 删除
    obtain = db.Column(db.Boolean)  # 已经获奖
    name = db.Column(db.String(140))  # 礼物名称
    time = db.Column(db.DateTime)  # 抽奖时间
    score = db.Column(db.Integer)  # 消耗积分

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User, backref='gift')
