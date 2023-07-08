# Python 3.7.7
teBetalen = 0
nogEenProduct = "ja"
while nogEenProduct == "ja":
    print("Wat is de prijs van het product dat u koopt?")
    prijs = float(input())
    teBetalen = teBetalen + prijs
    print("Wilt u nog een product invoeren?")
    nogEenProduct = input()
print("TOTAAL: " + str(teBetalen) + " EUR")
