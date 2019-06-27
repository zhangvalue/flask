# *===================================*
# -*- coding: utf-8 -*-
# * Time : 2019-06-27 17:06
# * Author : zhangsf
# *===================================*
from flask import Flask, session
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 配置7天有效


# 设置session
@app.route('/')
def set():
    session['username'] = 'zhangvalue'  # 设置“字典”键值对
    session.permanent = True  # 设置session的有效时间，长期有效，一个月的时间有效，
    # 具体看上面的配置时间具体的，没有上面设置的时间就是一个月有效
    print(app.config['SECRET_KEY'])
    return 'success'


# 读取session
@app.route('/get')
def get():
    # 第一种session获取如果不存在会报错
    # session['username']
    # 推荐使用session.get('username')
    # session.get('username')
    return session.get('username')


# 删除session
@app.route('/delete/')
def delete():
    print(session.get('username'), session.pop('username', None))
    # 或者 session['username'] = False
    print(session.get('username'))
    return 'success'


# 清除session中所有数据
@app.route('/clear')
def clear():
    print(session.get('username'))
    # 清除session中所有数据
    session.clear
    print(session.get('username'))
    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5010')
