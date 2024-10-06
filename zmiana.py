inwokacja = 'Litwo, Ojczyzno moja! ty jesteś jak zdrowie; Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie.'

x = input("Podaj literę do zmienienia lub usunięcia ")
y = x.lower()
z = x.capitalize()

a = str(input("na  jaką literę chcesz zmienić/by usunąć wpisz 0: "))

if a == '0':
    inwokacja = inwokacja.strip(y)
    inwokacja = inwokacja.strip(z)
else: 
    inwokacja = inwokacja.replace(y, a)
    inwokacja  = inwokacja.replace(z, a)
    
print(inwokacja)