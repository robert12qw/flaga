from flask import Flask, render_template

import wikipedia as wiki




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

import random
from moje_programy.character_wiki import character
@app.route('/brudnopis')
def brudnopis():
    super_heroes = ['Tygrysek', 'Sowa', "Kangurzątko", 'Kłapouchy' ]
    chosen_hero = random.choice( super_heroes)
    super_hero = character( chosen_hero)
    return render_template("brudnopis.html", hero=super_hero, super_heroes=super_heroes)

@app.route('/kubus_puchatek')
def kubus_puchatek():
	return render_template("kubus_puchatek.html")

if __name__=="__main__":
    app.run()
