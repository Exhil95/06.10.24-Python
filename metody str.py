# format
# replace
# lower 
# upper
# find, 
# is____
# strip, 
# lstrip, 
# rstrip
# join

inwokacja = "Litwo, Ojczyzno moja! ty jesteś jak zdrowie; Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie. {}"

inw = inwokacja.format(inwokacja)
print(inw)
print()

inw2 = inwokacja.replace('L',  'M')
print(inw2)
print()

inw3 = inwokacja.lower()
print(inw3)
print()

inw4 = inwokacja.upper()
print(inw4)
print()

inw5 = inwokacja.find('Ojczyzno')
print(inw5)
print()

inw6 = inwokacja.istitle()
print(inw6)
print()

inw7 = inwokacja.strip('a')
print(inw7)
print()

inw8 = inwokacja.lstrip('L')
print(inw8)
print()

inw9 = inwokacja.rstrip('!')
print(inw9)
print()

inw10 = " ".join([inwokacja, 'a'])
print(inw10)
print()

