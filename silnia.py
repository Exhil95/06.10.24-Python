x = int(input("Podaj liczbę z której chcesz wyciągnąć silnię: "))

def silnia(x):
    if x == 0:
        return 1
    else:
        return x * silnia(x-1)

y = silnia(x)

print(y)
