import requests

link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text 

kubus_text = kubus_text.replace('<p>', ' ') 
kubus_text = kubus_text.replace('</p>', ' ')

dlugosc_kubusia = len(kubus_text)
print (dlugosc_kubusia)

kubus_puchatek_slowa = kubus_text.split()
kubus_puchatek_slowa_n = len(kubus_puchatek_slowa)
print (kubus_puchatek_slowa_n)

kubus_n = 0
for i, s in enumerate(kubus_puchatek_slowa):
	print(i, s, ' ', s.replace('a', 'xD'))



	#if s == 'Kubuś':
	#	print (i, s)		
	#	kubus_n =kubus_n+1
#	if 'Kubuś' in s:
#		print(i,s)
#		kubus_n +=1
print(kubus_n)


