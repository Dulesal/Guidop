import time
class PosteRadioView:
    __radioState = False

    def update(self, fonction, var):
        if (fonction == "message"):
            self.afficherMessage(var)
        elif (fonction == "etat"):
            self.setRadioState(var)


    def afficherMessage(self, message):
        if (self.__radioState):
            print(f"\033[92m{message}\033[0m")

    def setRadioState(self, state):
        if (self.__radioState != state):
            self.__radioState = state
            if(state):
                print("The radio turns on ...")
                time.sleep(1)
            else:
                print("The radio turns off ...")
                time.sleep(1)

        print(f"")