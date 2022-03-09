from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    text = open('xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/flaga_dla_ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga_dla_ukrainy.html")


@app.route('/nowy')
def nowy():
    return 'nowy!'

@app.route('/kubus_puchatek')
def kubus_puchatek():
	return render_template("kubus_puchatek.html")


@app.route('/brudnopis')
def brudnopis():
    return render_template("brudnopis")

if __name__=="__main__":
    app.run()
