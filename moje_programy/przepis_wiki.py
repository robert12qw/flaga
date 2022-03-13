import wikipedia as wiki
wiki.set_lang("pl")

def przepis( name):
    content = wiki.summary(name, sentences=6)
    return content