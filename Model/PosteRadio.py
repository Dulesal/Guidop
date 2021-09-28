class PosteRadio:
    __auditeur = None
    __messageEntendu = ""
    __observer = None

    def __init__(self, message):
        self.__messageEntendu = message

    def setChanged(self, fonction , var):
        self.__observer.update(fonction, var)

    def addObserver(self, observer):
        self.__observer = observer
