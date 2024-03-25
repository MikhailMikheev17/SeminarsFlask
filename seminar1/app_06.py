"""Задание №6
Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст."""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    students = [
        {
            'first_name': 'Mikhail',
            'last_name' : 'Mikheev',
            'age' : 24 ,
            'average_score' : '4.3' 
        },
        {
            'first_name': 'Semen',
            'last_name' : 'Yastrebov',
            'age' : 23 ,
            'average_score' : '4.5' 
        },
        {
            'first_name': 'Danil',
            'last_name' : 'Kardilianov',
            'age' : 23,
            'average_score' : '4.0' 
        }
    ]

    context = {
        'person' : students 
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)