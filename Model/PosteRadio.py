from Model import StationRadio


class PosteRadio:
    __auditeur = StationRadio()
    __messageEntendu = ""

    def __init__(self, message):
        self.__messageEntendu = message
