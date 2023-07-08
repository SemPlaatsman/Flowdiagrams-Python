# Python 3.7.7
kosten = 0
print("Wat is uw leeftijd?")
leeftijd = float(input())
if leeftijd > 3:
    print("Welk seizoen is het nu? (hoog/laag)")
    seizoen = input()
    if seizoen == "laag":
        kosten = kosten + 38
    else:
        kosten = kosten + 40
    print("Heeft u een beperking? (ja/nee)")
    beperking = input()
    if beperking == "ja":
        pass
    print("Betaalt u online of aan de kassa? (online/kassa)")
    betaling = input()
    if betaling == "kassa":
        if leeftijd < 60:
            if beperking == "ja":
                pass
            else:
                kosten = kosten + 2
print("De toegang kost u: " + str(kosten) + " euro")
