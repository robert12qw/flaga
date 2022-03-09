from flask import Flask, render_template



from moje_programy.character_wiki import character

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

@app.route('/brudnopis')
def brudnopis():

    moj_super_hero = tygrysek
    super_hero = character(moj_super_hero)
    super_hero2 = character2()

    return render_template("brudnopis.html", hero=super_hero, hero2=super_hero2)



    @app.route('/kubus_puchatek')
def kubus_puchatek():
	return render_template("kubus_puchatek.html")

if __name__=="__main__":
    app.run()
