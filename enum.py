from enum import Enum

class  RodzajSilnika(Enum):
    benzynowy = 1
    diesel = 2
    elektryczny = 3

silnik = input("Podaj rodzaj swojego silnika: ")