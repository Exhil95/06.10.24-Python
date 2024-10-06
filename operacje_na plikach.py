# sciezkaPliku = "myInput.txt"
bezwzglednaSciezka = "C:\\Users\\dkucz\\OneDrive\\Pulpit\\kurs python\\06.10.24 Python\\myInput.txt"
with open(bezwzglednaSciezka) as f:
    listaLinii: list[str] = f.readlines()
print(listaLinii)
kopia = []

for i in listaLinii:
    kopia.append(i.replace('i', 'x').replace('e', 'x').replace('a', 'x'))
    
print(kopia)

nazwa_nowego_pliku = bezwzglednaSciezka.replace('myInput', 'myOutput')
with open(nazwa_nowego_pliku, 'x') as f_output:
    f_output.writelines(kopia)

wynik = "wzystko ok" if nazwa_nowego_pliku == "poprawna nazwa" else "błąd"
print(wynik)


wynik = 15
match(wynik):
    case 2:
        print("to dwójka")
    case 3:
        print("to trójka")
    case _:
        print("nie ma takiej liczby")
        