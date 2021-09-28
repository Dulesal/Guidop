class Resistant:
    __nom = ""
    __parole = ""

    def __init__(self, nom, parole):
        self.__nom = nom
        self.__parole = parole

    def getNom(self):
        return self.__nom

    def getParole(self):
        return self.__parole