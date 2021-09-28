import random
from View.StationRadioView import StationRadioView


class StationRadio:
    __nom: str
    __resistant: []
    __observer: StationRadioView
    __etat: bool = False

    def __init__(self, nom, resistant):
        self.__nom = nom
        self.__resistant = resistant

    def setChanged(self, etat):
        self.__etat = etat

    def notifyObserver(self, var):
        if (self.__etat):
            self.__observer.update(var)
            self.__etat = False

    def addObserver(self, observer):
        self.__observer = observer

    def diffuserMessage(self):
        alea = random.randint(0, (len(self.__resistant) - 1))
        return self.__resistant[alea].getParole()