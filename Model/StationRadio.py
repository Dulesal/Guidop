import time
class StationRadio:
    __radio = None
    __name = ""
    __messages = ""

    def __init__(self, name, paroles):
        self.__name = name
        self.__messages = paroles

    def diffuserMessage(self):
        messages = self.__messages.split(" ")
        for message in messages:
            print(f"{message} ", end='')
            time.sleep(0.35)
