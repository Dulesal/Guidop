class PosteRadio:
    __auditeur = None
    __messageEntendu = ""

    def __init__(self, message):
        self.__messageEntendu = message

    def listen(self):
        self.__auditeur