# from crypt import methods
from flask import Flask

# initialize Flask
app = Flask(__name__)


# Home route
@app.route('/',methods=['GET'])
def greet():
    return 'Hi there!'


# about route
@app.route('/about', methods=['GET'])
def about():
    return 'This is the about page. What do you wanna know?'


# variable route
@app.route('/<string:var>/', methods=['GET'])
def var_route(var):
    return ({
        'name': var
    })

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=4500)