from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/<string:text>/')
def string(text):
    return str(len(text))

if __name__ == '__main__':
    app.run(debug=True)