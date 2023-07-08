# Python 3.7.7
import random

random.seed()   #Prepare random number generator

aantalGeraden = 0
geheimeGetal = int(random.random() * 10) + 1
print("Ik heb een getal van 1 t/m 10 in mijn hoofd. Wat denk jij dat het getal is?")
geradenGetal = int(input())
aantalGeraden = aantalGeraden + 1
while geradenGetal > 10 or geradenGetal < 1:
    print("Ik zei toch een getal tussen de 1 en de 10! Doe maar weer opnieuw")
    geradenGetal = int(input())
    aantalGeraden = aantalGeraden + 1
while geheimeGetal != geradenGetal:
    if geradenGetal < geheimeGetal:
        print("Het getal dat ik in mijn hoofd heb ik is hoger dan het geraden getal")
        aantalGeraden = aantalGeraden + 1
    else:
        print("Het getal dat ik in mijn hoofd heb is lager dan het geraden getal")
        aantalGeraden = aantalGeraden + 1
    geradenGetal = int(input())
    while geradenGetal > 10 or geradenGetal < 1:
        print("Ik zei toch een getal tussen de 1 en de 10! Doe maar weer opnieuw")
        geradenGetal = int(input())
        aantalGeraden = aantalGeraden + 1
print("Je hebt er " + str(aantalGeraden) + " keer over gedaan, goed gespeeld")
