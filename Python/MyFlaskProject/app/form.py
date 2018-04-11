# 表单文件
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    username = StringField('用户名(Account)', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('密码(Password)', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class RegisterForm(FlaskForm):
    username = StringField('用户名(Account)', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('密码(Password)', validators=[DataRequired()])
    email = StringField('电子邮件(Email)', validators=[DataRequired(), Length(1, 64), Email()])


class PostForm(FlaskForm):
    title = StringField('博客题目(Name)', validators=[DataRequired(), Length(1, 255)])
    body = TextAreaField('博客内容(Description)', validators=[DataRequired(), Length(1, 65536)])


class EditForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
