lista1 = ['Adam', 'Bogdan', 'Celina', 'Daniel', 'Eliza', 'Florian']
lista2 =  ['Grzegorz', 'Hieronim', 'Inga', 'Jolanta', 'Karol', 'Leszek', 1, 2, 4, 5]

for i in lista1:
    print(i)
    
for i in lista2:
    print(i)
        
def wiekszyOX(iloscElelmentow, oIleWiekszy):
    lista =  []
    for ktoraIteracja in range(0,  iloscElelmentow*oIleWiekszy, oIleWiekszy):
        lista.append(ktoraIteracja)
    print(lista, len(lista))

wiekszyOX(21, 2)
