#import / biblioteki
import requests #biblioteka w ogóle, pip3, dokumentacja, wersja.
link = 'http://zajecia-programowania-xd.pl/flagi'
flagi_response = requests.get(link)
flagi_tekst =  flagi_response.text
print (flagi_tekst)



flagi = flagi_tekst.split('</p>')
for f in flagi:
#	if 'http://' in f:
		f = f[3:]
		print('-',f)

#LISTE_ELEMENTOW = ['1', '2', '3',]

#flagi = ['link1', 'link2','link3']
# Listy

#lista = [1, 2, 3] #int (integer)elementy po przecinku 
#lista = ['1','2', '3'] #str (string)
#lista = 'abcdefg' #albo kolejne znaki w stringu
#######  0123456


#dlugosc_listy = len(lista)
#print ('Dlugosc:', dlugosc_listy)

#element = lista[1]
#print ('element:', element)

#Pętli
#for i in lista:
#	print (i)
