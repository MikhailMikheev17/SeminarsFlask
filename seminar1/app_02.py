"""Задание №2
Дорабатываем задачу 1.
Добавьте две дополнительные страницы в ваше вебприложение:
○ страницу "about"
○ страницу "contact"."""


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/about/')
def about():
    return 'My name is Mikhail!'

@app.route('/contact/')
def contact():
    return 'My number:999 999 999 !'


if __name__ == '__main__':
    app.run(debug=True)