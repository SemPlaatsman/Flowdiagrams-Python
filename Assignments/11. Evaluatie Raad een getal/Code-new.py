# Python 3.7.7
import random

random.seed()   #Prepare random number generator

while True:    #This simulates a Do Loop
    aantalGeraden = 0
    print("Wat wilt u als minimum getal?")
    minimum = int(input())
    print("Wat wilt u als maximum getal?")
    maximum = int(input())
    verschil = maximum - minimum
    geheimeGetal = int(random.random() * verschil) + minimum
    print("Ik heb een getal tussen de " + str(minimum) + " en de " + str(maximum) + " in mijn hoofd. Wat denk jij dat het getal is?")
    geradenGetal = int(input())
    aantalGeraden = aantalGeraden + 1
    while geradenGetal > maximum or geradenGetal < minimum:
        print("Ik zei toch een getal tussen de " + str(minimum) + " en de " + str(maximum) + "! Doe maar weer opnieuw.")
        geradenGetal = int(input())
        aantalGeraden = aantalGeraden + 1
    stoppen = "ja"
    while geheimeGetal != geradenGetal and stoppen == "ja":
        if geradenGetal < geheimeGetal:
            print("Het getal dat ik in mijn hoofd heb is hoger dan het geraden getal. Wil je verder spelen? (ja/nee)")
            stoppen = input()
            while stoppen != "nee" and stoppen != "ja":
                print("Je moet wel ja of nee invullen! Wil je verder spelen? (ja/nee)")
                stoppen = input()
            aantalGeraden = aantalGeraden + 1
        else:
            print("Het getal dat ik in mijn hoofd heb is lager dan het geraden getal. Wil je verder spelen? (ja/nee)")
            stoppen = input()
            while stoppen != "nee" and stoppen != "ja":
                print("Je moet wel ja of nee invullen! Wil je verder spelen? (ja/nee)")
                stoppen = input()
            aantalGeraden = aantalGeraden + 1
        if stoppen == "ja":
            print("Wat denk je nu dat het getal is?")
            geradenGetal = int(input())
            while geradenGetal > maximum or geradenGetal < minimum:
                print("Ik zei toch een getal tussen de " + str(minimum) + " en de " + str(maximum) + "! Doe maar weer opnieuw.")
                geradenGetal = int(input())
                aantalGeraden = aantalGeraden + 1
    if stoppen == "nee":
        print("Bedankt voor het spelen. Jammer dat je het niet meer leuk vond.", end='', flush=True)
    else:
        print("Gefeliciteerd, je hebt er " + str(aantalGeraden) + " keer over gedaan totdat je het getal hebt geraden.", end='', flush=True)
    print(". Wilt u nog eens spelen? (ja/nee)")
    herhaling = input()
    if not(herhaling == "ja"): break   #Exit loop
print("Het spel in beëindigd.")
