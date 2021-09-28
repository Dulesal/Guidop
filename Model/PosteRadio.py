from Model.StationRadio import StationRadio
from View.PosteRadioView import PosteRadioView


class PosteRadio:
    __station: StationRadio
    __messageEntendu: str
    __observer: PosteRadioView
    __etat: bool = False

    def __init__(self, message):
        self.__messageEntendu = message

    def setChanged(self, etat):
        self.__etat = etat

    def notifyObserver(self, fonction, var):
        if (self.__etat):
            self.__observer.update(fonction, var)
            self.__etat = False

    def addObserver(self, observer):
        self.__observer = observer
