# Python 3.7.7
import random

random.seed()   #Prepare random number generator

kopMunt = int(random.random() * 2)
if kopMunt == 0:
    print("Het is kop")
else:
    print("Het is munt")
