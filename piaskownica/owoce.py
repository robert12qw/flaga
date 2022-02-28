  # Lista
lista = []
lista = [1, 2, 3]
lista = [1, 2, 3, 4] #cyfry typ: int (integer)
koszyk = ['jablko1','jablk2', 'jablko3', 'garść malin'] # napisy typ: str (string) 

#Pętla
print ()
print ()
print ('zaczynam')
print ()	
for owoc in koszyk:

	print ('1. Wyciągam', owoc)
	print ('2. Myje', owoc)
	print ('3. Zjadam', owoc)

	if owoc == 'garść malin':
		continue

	print ('4.  Wyrzucam ogryzek po', owoc)
	print ()
print ('skończyłem')
print ()
