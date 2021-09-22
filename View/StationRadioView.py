import time
class StationRadioView:
    def update(self, fonction, var):
        if (fonction == "message"):
            self.afficherMessage(var)
        elif (fonction == "etat"):
            self.setRadioState(var)


    def afficherMessage(self, message):
        print(f"\033[92m{message}\033[0m")
