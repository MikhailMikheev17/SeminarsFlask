"""Задание №8
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
"""
from flask import Flask, flash, redirect, render_template,request, url_for,redirect

app = Flask(__name__)

app.secret_key = '0a10eea4ada16eb5f16f97df56e12ad036d31199370d8788c9f8104f20bc428e'

@app.route('/', methods=['GET', 'POST'])
def age_validate():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('age_validate'))
        
    return render_template('form_flash.html')   



if __name__ == '__main__':
    app.run(debug=True)