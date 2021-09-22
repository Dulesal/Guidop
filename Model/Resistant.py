class Resistant:
    __name = ""
    __parole = ""

    def __init__(self, name, parole):
        self.__name = name
        self.__parole = parole

    def getName(self):
        return self.__name

    def getParole(self):
        return self.__parole