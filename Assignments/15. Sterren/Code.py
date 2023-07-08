# Python 3.7.7
aantal = int(input("Hoeveel sterren?"))
for rij in range(1,aantal+1):
    for rij2 in range(1,rij+1):
        print("* ",end = "")
    print()
