import requests

# Pobranie tekstu ze strony (jako tafla tesktu).
orangutan = 'https://zajecia-programowania-xd.pl/flagi'
surowe_info = requests.get( orangutan)
text = surowe_info.text

# Przygotowanie listy linków ze strony :)
lista_linii = text.split('</p>')
linki = []
for linia in lista_linii:

    link = linia.replace('<p>', '')
    link = link.replace('- ', '')
    link = link.strip()
    if ' ' in link or '<' in link:
        continue
    linki.append( link)

# ZADANIE DOMOWE DODATKOWE:
# Napisz funkcje która zadanej liście zliczy
# Wszystkie elementy które mają '.pl' ale tylko '.pl' a nie 
# np. '.eu.pl', '.site.pl', '.com.pl' < --- tych nie zliczamy.
# Czyli funkcja bierze listę stringów z domenami
# Zlicza same '.pl'
# Zwraca liczbe samych '.pl'

# Możesz użyć poniższego przykładu i wcześniejszych kodów aby rozwiązać zadanie.
def policz_domeny_pl(lista):
    licz=0
    for i, adres in enumerate(lista):
        if '.com.pl' in adres:
           continue
        elif '.pl' in adres:
            licz += 1
    return licz

wynik = policz_domeny_pl(linki)
print(wynik )