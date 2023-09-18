'''
@Project ：Dimension_reduction.py 
@File    ：app.py
@IDE     ：PyCharm 
@Author  ：成佳闻
@Date    ：2023/9/17 18:36 
'''


#(Flask) D:\PycharmProjects\watchlist>flask run      在命令行输入
from flask import Flask,url_for,render_template
app=Flask(__name__)
# @app.route('/Komorebi')
# @app.route('/')
# @app.route('/home')
# def Hello():
#     return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
#
# @app.route('/user/<name>')
# def user_page(name):
#     return '你好，初次见面，请多多指教！'
#
#
# @app.route('/test')
# def test_url_for():
#     print(url_for('Hello'))
#     print(url_for('user_page',name='Komorebi'))
#     print(url_for('test_url_for'))
#     return url_for('user_page',name='Komorebi')
#
# @app.route('/<any(student,class):url_path>/<id>/')
# def item(url_path, id):
#     if url_path == 'student':
#         return '学生{}详情'.format(id)
#     else:
#         return '班级{}详情'.format(id)


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

@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)