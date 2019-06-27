# *===================================*
# -*- coding: utf-8 -*-
# * Time : 2019-06-26 14:38
# * Author : zhangsf
# *===================================*
from flask import Flask, g

app = Flask(__name__)


@app.route('/99')
def hello_world():
    return 'Hello World!'


@app.route("/zhangvalue")
def zhagnvalue():
    return "hello zhangvalue666!"


# @app.route("/<user_name>")
# def user_name(user_name):
#     return 'hello %s!' % user_name

@app.route("/articles/<int:id>")
def articles(id):
    return 'articles %s!' % id

#before_first_request 处理第一次请求之前执行
@app.before_first_request
def bf_first_request():
    print("before_first_request ")


# 在服务器接收的请求还没分发到视图函数之前执行的钩子函数
#在每次请求之前执行. 通常使用这个钩子函数预处理一些变量, 视图函数可以更好调用

@app.before_request
def before_request():
    print("before_request  我勾住了每次请求")


@app.teardown_request
def teardown_request(error):
    print(error)
    print('teardown_request')

@app.after_request
def after_request(rsp):
    print(rsp)
    print('after_request')
    return rsp
if __name__ == '__main__':
    app.run(host='127.0.0.1',port='5006')
