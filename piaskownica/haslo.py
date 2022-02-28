import random
import string

# Generator Hasła
# - string - ciąg znaków
# - losowe hasło 
# - określona ilsc znakow - ponad 8
# - Duże litery, 2
# - Małe litery, 2
# - Znaki specjalne, 2
# - cyfry, 2

n_znakow = 8 
n_znakow_typu = 2

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
digits = string.digits
wszystkie_znaki = lowercase + uppercase + punctuation + digits

losowe_znaki = random.sample(wszystkie_znaki, n_znakow)

haslo = ''.join (losowe_znaki)

# zadanie domowe
# udoskonalić generator haseł tak aby:
# 1. brał po 2 losowe cyfry/znaki i duże/małe litery
# 2. losowa kolejnośćcyfr, znaków dużych i małych liter
# 3. pogłówkujcie aby to działało dla liczby znaków od 8 do 20 

# liczby znaków od 8 do 20

#zadanie trzymamy u siebie na serwerze i 
# W poniedziałek bedzie omowione jak bedzoiemy
#gromadzic zadania, domowe, projekty
# też pare słów o GIT i VSC
print()
print(haslo)
print()
