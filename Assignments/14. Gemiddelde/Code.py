# Python 3.7.7
som = 0
aantal = 0
getal = int(input("Geef een getal!"))
while getal != 0:
    som = int(som) + int(getal)
    aantal = aantal + 1
    getal = int(input("Geef nog een getal! Een 0 stopt de invoer."))
print("De som van alle getallen is " + str(som) + " en je hebt " + str(aantal) + " getallen ingevoerd.")
antwoord = str(input("Wil je het gemiddelde ook nog weten? (ja/nee)"))
if antwoord == "ja":
    gemiddelde = som / aantal
    print("Het gemiddelde is " + str(round(gemiddelde, 1)))
print("Bedankt voor het spelen!")
