'''
@Project ：Dimension_reduction.py 
@File    ：app.py
@IDE     ：PyCharm 
@Author  ：成佳闻
@Date    ：2023/9/17 18:36 
'''


#(Flask) D:\PycharmProjects\watchlist>flask run      在命令行输入
from flask import Flask,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import click


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


#创建用户信息表
class User(db.Model):# 表名将会是 user（自动生成，小写处理）
    id=db.Column(db.Integer,primary_key=True)# 主键
    name=db.Column(db.String(20))# 名字
#创建电影名称表
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year=db.Column(db.String(4))#年份


@app.cli.command()# 注册为命令
@click.option('--drop',is_flag=True,help='Create after drop.')
# 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:# 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialize the database')#输出提示信息


#创建自定义命令 forge
@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()
    name = 'Komorebi'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    user=User(name=name)
    db.session.add(user)
    for m in movies:
        movie=Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('Done')
@app.route('/')
def index():
    user=User.query.first()#读取用户信息
    movies=Movie.query.all()#读取电影信息
    return render_template('index.html',user=user,movies=movies)