from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to your home page!'


@app.route('/about')
def about():
    return 'Welcome to your about page!'


@app.route('/login')
def login():
    return 'Welcome to your login page!'


@app.route('/register')
def register():
    return 'Welcome to your register page!'


@app.route('/<page_name>')
def other_page(page_name):
    response = make_response("The page %s does not exist." %page_name, 404)
    return response

if __name__ ==  '__main__':
    app.run(debug=True)