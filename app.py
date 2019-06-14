from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/zhangvalue")
def zhagnvalue():
    return "hello zhangvalue666!"


@app.route("/<user_name>")
def user_name(user_name):
    if user_name == "zhang":
        return render_template('index.html', user_name=user_name)
    else:
        return render_template('index.html', user_name='zhangsf')


@app.route("/articles/<int:id>")
def articles(id):
    return 'articles %s!' % id


if __name__ == '__main__':
    app.run()
