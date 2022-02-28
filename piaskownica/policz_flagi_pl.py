from lista_flag import stworz_liste_flag

def policz_domeny_pl( lista_flag):
    wynik = 0
    # Tu zaczyna się Twój kod.
    for flaga in lista_flag:
        if '.pl' in flaga:
            wynik += 1
        
        print(flaga)
        # Tu kończy się Twój kod.
    return wynik

# Wyhaszuj na końcu te 2 linie
orangutan = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag( orangutan)
wynik = policz_domeny_pl( lista_flag)
print( wynik)