from enum import Enum 

class  RodzajSilnika(Enum):
    Spalinowy = 1
    Elektryczny = 2
    Gazowy = 3
    
# silnik = input("Podaj rodzaj swojego silnika: ") 

#  if RodzajSilnika[silnik.capitalize()] == RodzajSilnika.Spalinowy:
#      print("Twój silnik jest nieekologiczny")
#  else:
#      print("Twój silnik jest ekologiczny") 

print(RodzajSilnika.Elektryczny)
