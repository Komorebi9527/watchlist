'''
@Project ：Dimension_reduction.py 
@File    ：app.py
@IDE     ：PyCharm 
@Author  ：成佳闻
@Date    ：2023/9/17 18:36 
'''
from flask import Flask
from flask import url_for
app=Flask(__name__)
@app.route('/Komorebi')
@app.route('/')
@app.route('/home')
def Hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return '你好，初次见面，请多多指教！'


@app.route('/test')
def test_url_for():
    print(url_for('Hello'))
    print(url_for('user_page',name='Komorebi'))
    print(url_for('test_url_for'))
    return url_for('user_page',name='Komorebi')

@app.route('/<any(student,class):url_path>/<id>/')
def item(url_path, id):
    if url_path == 'student':
        return '学生{}详情'.format(id)
    else:
        return '班级{}详情'.format(id)

