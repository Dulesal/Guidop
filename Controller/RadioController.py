from Model.StationRadio import StationRadio


class RadioController:
    __stationRadio: StationRadio
    __posteRadio = []

    def addPosteRadio(self, PosteRadio):
        self.__posteRadio.append(PosteRadio)

    def addStationRadio(self, StationRadio):
        self.__stationRadio = StationRadio

    def run(self):
        self.startBroadcast()

    def startBroadcast(self):
        message = self.__stationRadio.diffuserMessage()
        self.__stationRadio.setChanged(True)
        self.__stationRadio.notifyObserver(message)

        for poste in self.__posteRadio:
            poste.setChanged(True)
            poste.notifyObserver("etat", True)
            poste.setChanged(True)
            poste.notifyObserver("message", message)
            poste.setChanged(True)
            poste.notifyObserver("etat", False)