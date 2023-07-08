# Python 3.7.7
print("Wat is de huidige temperatuur?")
temperatuur = int(input())
print("Op welke temperatuur stel je de thermostaat in?")
thermostaat = int(input())
if temperatuur >= thermostaat:
    print("De verwarming hoeft niet aan. De temperatuur is hoog genoeg")
else:
    while temperatuur < thermostaat:
        print(str(temperatuur) + "...er wordt 1 graad verwarmd...")
        temperatuur = temperatuur + 1
    print("Gewenste temperatuur van " + str(temperatuur) + " bereikt!")
