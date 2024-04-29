from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/')
def index():
    return '<html><body><h1>Hello world</h1></body></html>'

@app.route('/about')
def about():
    return '<h1> About Page </h1>'

if __name__ == '__main__':
    app.run(debug=True)