import os
import uuid
import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@127.0.0.1/movie"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:password@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SECRET_KEY'] = 'dad9c4cbb6a449cc8436b7b78e077341'
# 定义文件上传保存的路径，在__init__.py文件所在目录创建media文件夹，用于保存上传的文件
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/media/')

# 定义db对象，实例化SQLAlchemy，传入app对象
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 注册蓝图
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


# 添加全局404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
