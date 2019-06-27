# *===================================*
# -*- coding: utf-8 -*-
# * Time : 2019-06-26 15:11
# * Author : zhangsf
# *===================================*
# encoding:utf-8
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')  # 首页
def index():
    login_url = url_for('login')
    print("这是首页")
    return redirect(login_url)  # 重定向为登录页面
    return u'这是首页'


@app.route('/login/')  # 登录页面
def login():
    return u'这是登录页面'


@app.route('/question/<is_login>')  # 问答页面
def question(is_login):
    if is_login == '1':
        return u'这是问答页面'
    else:
        return redirect(url_for('login.index'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='80', debug=True)
