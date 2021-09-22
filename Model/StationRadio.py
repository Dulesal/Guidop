import time
class StationRadio:
    __radio = None
    __name = ""
    __resistant = []
    __observer = None

    def __init__(self, name, resistant):
        self.__name = name
        self.__resistant = resistant

    def setChanged(self, vue):
        self.__observer.update(vue)

    def addObserver(self, observer):
        self.__observer = observer


    def diffuserMessage(self):

        for resistant in self.__resistant:
            print(f"\n\033[93m{resistant.getName()} :", end='')
            paroles = list(resistant.getParole())
            for message in paroles:
                time.sleep(0.1)
                print(f"\033[93m{message}\033[0m", end='')
