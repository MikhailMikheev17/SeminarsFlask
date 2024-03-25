"""Задание №5
Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!"."""


from flask import Flask

app = Flask(__name__)

first ="""
<h1>Моя первая HTML страница</h1>
<p>Привет, мир!</p>
"""

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/html')
def html():
    return first






if __name__ == '__main__':
    app.run(debug=True)