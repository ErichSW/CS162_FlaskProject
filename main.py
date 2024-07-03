from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/top_left")
@app.route("/top_left")
def top_left():
    return render_template('top_left.html')

@app.route("/top_right")
@app.route("/top_right")
def top_right():
    return render_template('top_right.html')

@app.route("/bottom_left")
@app.route("/bottom_left")
def bottom_left():
    return render_template('bottom_left.html')