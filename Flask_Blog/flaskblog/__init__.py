import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)  # 创建app对象
app.debug = True  # 开启调试模式


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# 定义db对象，实例化SQLAlchemy，传入app对象
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# 定义登录管理对象
login_manager = LoginManager(app)
# 设置登录视图名称(未登录用户访问需要登录的页面会跳转到users.login这个视图,即跳转到登录页面)
login_manager.login_view = 'users.login'
# 自定义闪现消息(默认为Please log in to access this page)
# login_manager.login_message = '请登录再访问这个页面'
# 定义消息分类(info, success, danger, warning...)
login_manager.login_message_category = 'info'


# 邮箱设置
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


from flaskblog.users import users
from flaskblog.posts import posts
from flaskblog.main import main


# 注册蓝图
app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(posts)



# 添加全局404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


