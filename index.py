from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
   return render_template("index.html")

@app.route("/<name>")
def hi(name):
   return render_template("index.html", userName=name)
