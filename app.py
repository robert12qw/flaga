from flask import Flask, render_template
import os

app=Flask(__name__)

@app.route('/')
def index():
    text = 'czesc tu robert'
    return render_template("index.html", text=text)

if __name__=="__main__":
    app.run()
