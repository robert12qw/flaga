from flask import Flask, render_template
from moje_programy.character_wiki import character
from moje_programy.open_poem import open_poem
import random
import wikipedia as wiki

app=Flask(__name__)

@app.route('/')
def index():
    text = open('xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/flaga-dla-ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga-dla-ukrainy.html")
#https://pl.tradingview.com/widget/advanced-chart/   ----wykres kursy RUB/USD

@app.route('/xd')
def xd():
    return render_template("xd.html")




@app.route('/ciekawe-postacie')
def ciekawe_postacie():
    lista_ciekawych_postaci = [
        'Pudzianowski',         # 0
        'Małysz',               # 1
        'Kopernik',             # 2
        'Maria Skłodowska',     # 3
        'Kościuszko',           # 4
        'Donald',               # 5
        'Myszka Miki',          # 6
    ]
    opisy_postaci = []
    for i in range(3):
        postac = random.choice(lista_ciekawych_postaci)
        indeks = lista_ciekawych_postaci.index(postac)
        lista_ciekawych_postaci.pop(indeks)

        opis_postaci = character(postac)
        info = [postac, opis_postaci]
        opisy_postaci.append(info)

    return render_template("ciekawe-postacie.html", opisy_postaci=opisy_postaci)







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


#import random
#from moje_programy.open_lista_składników import open_poem
#from moje_programy.przepis_wiki import przepis
#@app.route('/3przepisy')
#def przepisy():
 #   potrawy = ['chałka', 'budyń', 'chleb']
  #  wybrana_potrawa = random.choice( potrawy )
   # poem_lines = open_poem()
    #description = przepis( wybrana_potrawa).encode('utf-8').decode()
   # return render_template("3przepisy.html", potrawa=wybrana_potrawa, 
#description=description, poem_lines=poem_lines)



@app.route('/kubus_puchatek')
def kubus_puchatek():
	return render_template("kubus_puchatek.html")

if __name__=="__main__":
    app.run()
