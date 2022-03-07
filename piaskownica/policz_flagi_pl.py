from lista_flag import stworz_liste_flag

def policz_domeny_pl( lista_flag):
    wynik = 0
    # Tu zaczyna się Twój kod.
    for flaga in lista_flag:
        if flaga.endswith('.pl'):
            wynik += 1
    return wynik

def policz_domeny_samo_com( lista_flag):
    wynik = 0
    # Tu zaczyna się Twój kod.
    for flaga in lista_flag:
        podzielona_flaga=flaga.split(".")
   
        if len(podzielona_flaga) == 2:
           # print("flaga dwuelementowa "+ str(podzielona_flaga) )
            if podzielona_flaga[1]== "com":
                wynik += 1
    return wynik
        
def policz_ilosc_a( lista_flag):
    licznik = 0
    # Tu zaczyna się Twój kod.
    for domena in lista_flag:
        for znak in domena:
            if znak == "a":
                licznik += 1
    return licznik

def znajdz_najkrotsze(lista_flag):
    min = lista_flag[0]
    for domena in lista_flag:
        dlugosc_domeny = len(domena)
        dlugosc_najkrutszej_domeny = len(min)
        if dlugosc_domeny < dlugosc_najkrutszej_domeny:
            if dlugosc_domeny > 0:
                 min = domena

    return min


orangutan = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag( orangutan)
wynik = policz_domeny_pl( lista_flag)
licznik= policz_ilosc_a (lista_flag)
min= znajdz_najkrotsze(lista_flag)

print("funkcja policz_domeny_pl zwróciła: " + str(wynik))
print("funkcja policz_domeny_samo_com zwróciła: " + str(policz_domeny_samo_com(lista_flag)))
print ("funkcja policz_ilosc_a zwróciła: "+ str(licznik))
print( "znajdz_najkrotsze: " + str(min))
