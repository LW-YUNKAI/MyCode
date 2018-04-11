# 跨站点请求伪造保护
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# 数据库文件路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
