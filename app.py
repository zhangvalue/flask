# *===================================*
# -*- coding: utf-8 -*-
# * Time : 2019-06-27 12:34
# * Author : zhangsf
# *===================================*
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')  # 代表首页
def index():  # 视图函数
    return render_template('register.html')


@app.route('/center/add')  # 代表个人中心页
def center():  # 视图函数
    if request.method == 'GET':  # 请求方式是get
        name = request.args.get('name')  # args取get方式参数
        age = request.args.get('age')
        hobby = request.args.getlist('hobby')  # getlist取一键多值类型的参数
        return "姓名：%s 年龄：%s 爱好：%s" % (name, age, hobby)
    elif request.method == 'POST':
        name = request.form.get('name')  # form取post方式参数
        age = request.form.get('age')
        hobby = request.form.getlist('hobby')  # getlist取一键多值类型的参数
        return "姓名：%s 年龄：%s 爱好：%s" % (name, age, hobby)

app.config['DEBUG'] = True

if __name__ == '__main__':
    # 0.0.0.0代表任何能代表这台机器的地址都可以访问
    app.run(host='0.0.0.0', port=5005)  # 运行程序

