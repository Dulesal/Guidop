import time
class StationRadioView:
    __radioState = False

    def update(self, var):
        self.afficherMessage(var)

    def afficherMessage(self, message):
        print(f"\033[96mRadio diffuse: {message}\033[0m")