# *===================================*
# -*- coding: utf-8 -*-
# * Time : 2019-06-27 12:37
# * Author : zhangsf
# *===================================*
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from flask import send_from_directory

app = Flask(__name__)

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# 判断上传的文件是否是允许的后缀
def allowed_file(filename):
    return "." in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':  # 请求方式是get
        return render_template('upload.html')  # 返回模板
    else:
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files.get('file')  # 获取文件

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # 用这个函数确定文件名称是否是安全 （注意：中文不能识别）
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # 保存文件
            return redirect(url_for('show',
                                    filename=filename))


# 展示图片
@app.route('/show/<filename>')
def show(filename):
    # send_from_directory可以从目录加载文件
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    # 0.0.0.0代表任何能代表这台机器的地址都可以访问
    app.run(host='0.0.0.0', port=5006)  # 运行程序


