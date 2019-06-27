# *===================================*
# -*- coding: utf-8 -*-
# * Time : 2019-06-27 12:46
# * Author : zhangsf
# *===================================*
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])  # 支持get、post请求
def register():  # 视图函数
    if request.method == 'GET':  # 请求方式是get
        return render_template('register2.html')  # 返回模板
    elif request.method == 'POST':
        name = request.form.get('name')  # form取post方式参数
        age = request.form.get('age')
        hobby = request.form.getlist('hobby')  # getlist取一键多值类型的参数
        return "姓名：%s 年龄：%s 爱好：%s" % (name, age, hobby)


app.config['DEBUG'] = True

if __name__ == '__main__':
    # 0.0.0.0代表任何能代表这台机器的地址都可以访问
    app.run(port=5007)  # 运行程序

