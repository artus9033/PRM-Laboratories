# TODO-PRM: 2a) ustaw obraz bazowy na python:3.10
FROM python:3.10

RUN apt update
RUN apt install -y wget vim nano

# TODO-PRM: 2a) ustaw obecny katalog pracy w kontenerze na /myapp/
...

# TODO-PRM: 2a) skopiuj plik requirements.txt do kontenera jako: /myapp/requirements.txt
# Uwaga: plik wymagany jest tylko tymczasowo na etapie budowania; należy zwrócić uwagę na to, że w 2b) zostanie podpięty wolumen
# pod tą samą ścieżką, co spowoduje nadpisanie tego pliku. Jest to efekt pożądany, gdyż na etapie budowania obrazu
# konieczne jest zainstalowanie zależności Python, jednakże na etapie budowania obrazu nie jest jeszcze możliwe podpięcie wolumenu.
...

# TODO-PRM: 2a) zainstaluj zależności Pythona; wskazówka: użyj opcji -r menedżera pip: pip install -r <sciezka-do-pliku-txt>
# Uwaga: kontener posiada zainstalowane 2 wersje Pythona 3: systemową oraz 3.10, dostarczoną z obrazem.
# Należy wymusić, aby PIP instalował pakiety dla wersji 3.10 poprzez wywołanie go z interpretera Python:
# zamiast pip ... powinno się wpisać /usr/local/bin/python3 -m pip ...
...

# TODO-PRM: 2b) wskaż, że ten kontener oczekuje podpięcia wolumenu pod katalog /myapp/ w systemie plików kontenera
# Wskazówka: użyj instrukcji VOLUME
...

# TODO-PRM: 2c) poinformuj, że ten kontener uruchamia usługę na porcie TCP 5000 - użyj instrukcji EXPOSE
...

ENTRYPOINT [ "/myapp/app.py" ]
