lista2 =  ["Grzegorz", "Hieronim", "Inga", "Jolanta", "Karol", "Leszek", 1, 2, 4, 5, "a", "b", "c"]

litery = [x for x in lista2 if isinstance(x, str)]
cyfry = [x for x in lista2 if isinstance(x, int)]


sortuj_litery = sorted(litery)
sortuj_cyfry = sorted(cyfry)

posortowana_lista = sortuj_cyfry + sortuj_litery

print(posortowana_lista)
