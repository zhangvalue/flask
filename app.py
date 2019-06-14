from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/zhangvalue")
def zhagnvalue():
    return "hello zhangvalue666!"


@app.route("/<user_name>")
def user_name(user_name):
    return 'hello %s!' % user_name

@app.route("/articles/<int:id>")
def articles(id):
    return 'articles %s!' % id




if __name__ == '__main__':
    app.run()
