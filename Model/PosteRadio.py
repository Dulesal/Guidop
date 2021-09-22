class PosteRadio:
    __auditeur = None
    __messageEntendu = ""
    __observer = None

    def __init__(self, message):
        self.__messageEntendu = message

    def setChanged(self, vue):
        self.__observer.update(vue)

    def addObserver(self, observer):
        self.__observer = observer
