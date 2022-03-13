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
from moje_programy.open_poem import open_poem
@app.route('/brudnopis')
def brudnopis():
    super_heroes = ['Bruce Lee', 'Kubuś Puchatek', 'Kopernik', 'Małysz']
    chosen_hero = random.choice( super_heroes)
    description = character( chosen_hero).encode('utf-8').decode()
    poem_lines = open_poem()
    return render_template("brudnopis.html", hero=chosen_hero, 
description=description, poem_lines=poem_lines)

import random
from moje_programy.character_przepisy import character
from moje_programy.open_lista_składników import open_poem
@app.route('/3przepisy')
def 3przepisy():
    super_heroes = ['chałka', 'budyń', 'chleb']
    chosen_hero = random.choice( super_heroes)
    description = character( chosen_hero).encode('utf-8').decode()
    poem_lines = open_poem()
    return render_template("3przepisy.html", hero=chosen_hero, 
description=description, poem_lines=poem_lines)






@app.route('/kubus_puchatek')
def kubus_puchatek():
	return render_template("kubus_puchatek.html")

if __name__=="__main__":
    app.run()
