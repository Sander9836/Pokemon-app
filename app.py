from flask import Flask, request, render_template

app = Flask(__name__)
#vertelt wat het endpoint is (wat moet de server uitveoren?)
# "/" equivalent flask.palletsprojects.com/ == flask.palletsprojects.com
@app.route("/<user>", methods=['GET', 'POST'])
def hello_world(user):
    return render_template('hello.html', name=user)

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login/login.html')

@app.route("/clickedbutton", methods=['GET', 'POST'])
def login():
    return {}