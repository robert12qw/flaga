# Flaga

#### 1. Login do serwera.

```
ssh nazwa_uzytkownika@adres_ip
```


PS: W trakcie instalacji gdy proces się zatrzymuje z zapytaniem "Do you want to continue? [Y/n]" na końcu, napisz "Y" aby przejść dalej.


#### 2. Uaktualniamy paczki (packages).

VPS Ubuntu 18/20 (Home i większość innych):
```
apt update
apt upgrade
```
AWS Ubuntu 18/20 (Home i większość innych):

PS: Akiwa, zróbcie z rootem odrazu ścieżkę to sudo pounikammy dla AWS 

```
sudo apt update
sudo apt upgrade
```

#### 3. Git.

VPS Ubuntu 18/20 (Home i większość innych):
```
apt install git
cd /var/www
git clone https://github.com/lukasz-test/flaga.git
cd flaga
python3 xD.py
```

AWS Ubuntu 18/20 (Home i większość innych):
```
apt install git
mkdir /var/www <---- to w AWS trzeba zrobić
cd /var/www
git clone https://github.com/lukasz-test/flaga.git
cd flaga
python3 xD.py
```


#### 4. Wewnątrz środowiska (env).

Tworzenie i aktywacja środowiska:
```
python3 -m venv flagaenv
source flagaenv/bin/activate
```

Tworzenie zmiennej:
```
export FLASK_APP=app.py
```

Edycja pliku z nazwą domeny. Po wywołaniu nano wpisz po spacji nazwę swojej domeny np (bez "www."): 
domena = nazwa_domeny.pl
```
nano settings.ini
```
Aby zapisać wciśnij ctrl+s
Aby zamknąć wciśnij ctrl+x


Instalacja wymaganych bibliotek.
```
pip3 install -r requirements.txt
```

Uruchom skrypt przygotowujący hosting w serwerze.
```
python3 xd.py
```

systemctl start flaga.service

#### 5. Restartujemy nginxa i serwisy.

```
systemctl daemon-reload
systemctl restart nginx
systemctl restart flaga.service
```


#### 6. Zmiana napisu.

Będąc w folderze flaga edytujemy zawartość pliku xd.txt.
```
cd /var/www/flaga
nano xd.txt
```

Przeładowujemy stronę.
```
systemctl daemon-reload
systemctl restart nginx
systemctl restart flaga.service
```



