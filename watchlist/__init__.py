'''
@Project ：Dimension_reduction.py 
@File    ：__init__.py
@IDE     ：PyCharm 
@Author  ：成佳闻
@Date    ：2023/9/24 23:27 
'''


from flask import Flask,url_for,render_template,request,redirect,flash
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import click
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user


WIN=sys.platform.startswith('win')
if WIN:# 如果是 Windows 系统，使用三个斜线
    prefix='sqlite:///'
else:# 否则使用四个斜线
    prefix='sqlite:////'

app=Flask(__name__)

#写入了一个 SQLALCHEMY_DATABASE_URI 变量来告诉 SQLAlchemy 数据库连接地址
#sqlite:////数据库文件的绝对地址
#使用 Windows 系统，上面的 URI 前缀部分需要写入三个斜线（即sqlite:/// ）
app.config['SQLALCHEMY_DATABASE_URI']=prefix+os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #关闭对模型修改的监控
# # 在扩展类实例化前加载配置
db=SQLAlchemy(app)

login_manager = LoginManager(app) # 实例化扩展类


@login_manager.user_loader
def load_user(user_id):# 创建用户加载回调函数，接受用户 ID 作为参数
    from watchlist.models import User
    user=User.query.get(int(user_id))
    return user



@app.context_processor
def inject_user():
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)


from watchlist import views, errors, commands

login_manager.login_view = 'login'