from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'HI! On the next pages u can see our shop' 

@app.route('/clothes/')
def clothes():
    clothes = [{
        'name' : 'T-shirt',
        'price' : '1000p',
        'description' : 'Comfortable, beautiful and 100% cotton'},
        {
        'name' : 'jeans',
        'price' : '2000p',
        'description' : 'Low—waisted jeans visually shorten the legs, while high-waisted jeans make them longer.The high percentage of elastane in the composition is responsible for the perfect fit, especially when it comes to skinny jeans and their variations.'
        }
    ]
    context = {
        'clothes' : clothes 
    }

    return render_template('clothes.html', **context)

@app.route('/jackets/')
def jachets():
    jackets = [{
        'name' : 'Anorak',
        'price' : '5000p',
        'description' : 'А windbreaker, usually short, designed for the windy off-season.'},
        {
        'name' : 'Down jacket',
        'price' : '10000p',
        'description' : 'jacket, insulated with a feather—down mixture.'
        }
    ]

    context = {
        'jackets' : jackets 
    }
    return render_template('jackets.html',**context)

@app.route('/shoes/')
def shoes():
    shoes = [{
        'name' : 'Ballet flats ',
        'price' : '1500р',
        'description' : 'a classic model of womens shoes with or without a small heel.'},
        {
        'name' : 'Deserts',
        'price' : '7000р',
        'description' : 'Boots with suede uppers, leather or rubber soles on laces with a pair of holes.'
        }
    ]

    context = {
        'shoes' : shoes 
    }
    return render_template('shoes.html', **context)


if __name__ == '__main__':
    app.run(debug=True)