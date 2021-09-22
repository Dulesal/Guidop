import time
import random
class StationRadio:
    __radio = None
    __name = ""
    __resistant = []

    def __init__(self, name, resistant):
        self.__name = name
        self.__resistant = resistant

    def setChanged(self, message):
        self.__observer.update(message)

    def addObserver(self, observer):
        self.__observer = observer

    def diffuserMessage(self):
        alea = random.randint(0,(len(self.__resistant)-1))
        return self.__resistant[alea].getParole()
