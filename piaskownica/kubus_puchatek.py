import requests

link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text #.encode('utf-8'))

kubus_linie_b = kubus_text.split('</p>')



#czyszczenie
kubus_linie = []
for l in kubus_linie_b:
				#print('surowe l', l)
				#l = l[5:]  #l to ciag znakow: str ('string')
	l = l.replace('<p>', '')
	l = l.strip()	
	kubus_linie.append(l)	


#wyswietlanie
koszyk = ['jablko', 'maliny', 'mango']


start = 100
end = 400

tajemniczy_bohater = 'Spiderman'
bohater_2 = 'dot Ms'
for index, linia in enumerate( kubus_linie):
	
	if index >= start and index < end:
	
		linia = linia.replace ('Kubus', tajemniczy_bohater)
		linia = linia.replace ('Puchatek', tajemniczy_bohater)
		linia = linia.replace ('Królik', bohater_2)		
		linia = '<p>' + linia + '</p>' 		
		print (linia)
		
print()
print('<p>Czytała Krystyna Czubówna</p>')				#if 'Kubus' in l:
						#	print(i, l)

print ( len( kubus_linie ) )
