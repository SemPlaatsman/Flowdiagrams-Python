# Python 3.7.7
import random

random.seed()   #Prepare random number generator

computer = int(random.random() * 3)
print("Wat kies je? (steen/papier/schaar)")
speler = input()
if computer == 0:
    keuzeComp = "steen"
else:
    if computer == 1:
        keuzeComp = "papier"
    else:
        keuzeComp = "schaar"
print("Computer kiest " + keuzeComp + "!")
if speler == keuzeComp:
    print("Het is gelijk!")
else:
    if speler == "steen" and keuzeComp == "schaar" or speler == "papier" and keuzeComp == "steen" or speler == "schaar" and keuzeComp == "papier":
        print("De speler wint!")
    else:
        print("De computer wint!")
