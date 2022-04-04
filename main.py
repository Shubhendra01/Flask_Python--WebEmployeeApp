from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my website"

@app.route("/home")
def home():
    return "Welcome to home Page"

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/gallery")
def gallery():
    return "Welcome to gallery Page"

if __name__ == "__main__":
    app.run()