import requests

def policz_znaki(string):
	dlugosc_stringu = len(string)
	return dlugosc_stringu
#1
#2
#3
#4 dzielenie ciągów znaków na kawłki
#spllit()


link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text #.encode('utf-8'))


#link_b = link.upper()

link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
ciag = "abcd abcd abcd abcd"
efekt = ciag.split("d")

print()
print(ciag)
print(efekt)
print()



