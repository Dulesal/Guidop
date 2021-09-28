from Model import FlotteAlliee


class Resistant:
    __nom: str
    __parole: str
    __flotteAlliee: FlotteAlliee

    def __init__(self, nom, parole, flotteAlliee):
        self.__nom = nom
        self.__parole = parole
        self.__flotteAlliee = flotteAlliee

    def getNom(self):
        return self.__nom

    def getParole(self):
        return self.__parole