# Python 3.7.7
import random
random.seed()
spelen = "ja"
while spelen == "ja":
    getal = int(random.random() * 10) + 1
    tafel = int(input("Welke tafel wil je oefenen?"))
    uitkomst = getal * tafel
    antwoord = int(input(str(getal) + " x " + str(tafel) + " = "))
    if uitkomst == antwoord:
        print("Je antwoord is goed!")
    else:
        print("Helaas! Je antwoord had moeten zijn: " + str(uitkomst))
    spelen = input("Wil je nog eens de tafels oefenen? (ja/nee)")
print("Bedankt voor het oefenen van de tafels!")
