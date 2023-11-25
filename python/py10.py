import enum

class Pythonista(str, enum.Enum):
    BDFL = "Guido"
    FLUFL = "Barry"

def greet(name):
    match name:
        case Pythonista.BDFL:
            print("Hi, Guido!")
        case _:
            print("Howdy, stranger!")

greet(Pythonista.BDFL)