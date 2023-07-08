# Python 3.7.7
tafel = int(input("Welke tafel wil je?"))
getal = 0
while getal < 10:
    getal = getal + 1
    uitkomst = getal * tafel
    print(str(getal) + " x " + str(tafel) + " = " + str(uitkomst))
