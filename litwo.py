inwokacja = 'Litwo, Ojczyzno moja! ty jesteś jak zdrowie; Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie.'
x = 0
samogloski =  ['a', 'e', 'i', 'o', 'u',  'y',  'ą', 'ę', 'ó', 'ę']

tekst = inwokacja.lower()


for litera in tekst:
    if litera in samogloski:
        x += 1

print(x)
print(tekst)

print("no i chuj")


# elo
# elo2