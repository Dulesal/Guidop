class RadioController:
    __stationRadio = None
    __posteRadio = []

    def addPosteRadio(self, PosteRadio):
        self.__posteRadio.append(PosteRadio)

    def addStationRadio(self, StationRadio):
        self.__stationRadio = StationRadio

    def run(self):
        self.startBroadcast()

    def startBroadcast(self):
        self.__stationRadio.diffuserMessage()