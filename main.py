from Controller.RadioController import RadioController
from Model.FlotteAlliee import FlotteAlliee
from Model.PosteRadio import PosteRadio
from Model.StationRadio import StationRadio
from View.PosteRadioView import PosteRadioView
from Model.Resistant import Resistant
from View.StationRadioView import StationRadioView


def main():

    #Creation des flottes alliees
    flotteAlliee1 = FlotteAlliee("Americains")
    flotteAlliee2 = FlotteAlliee("Angleterre")
    flotteAlliee3 = FlotteAlliee("Canada")

    #Creation des resistants
    resistant1 = Resistant("Jean", "Les chants les plus désespérés sont les chants les plus beaux",flotteAlliee1)
    resistant2 = Resistant("Patrick", "Message important pour Nestor: la girafe a un long cou",flotteAlliee2)
    resistant3 = Resistant("Marcel", "Les carottes sont cuites",flotteAlliee3)

    resistant = []
    resistant.append(resistant1)
    resistant.append(resistant2)
    resistant.append(resistant3)

    modelPosteRadio = PosteRadio("désespérés")
    viewPosteRadio = PosteRadioView()
    modelPosteRadio.addObserver(viewPosteRadio)

    modelStationRadio = StationRadio("BBC", resistant)
    viewStationRadio = StationRadioView()
    modelStationRadio.addObserver(viewStationRadio)

    controller = RadioController()
    controller.addStationRadio(modelStationRadio)
    controller.addPosteRadio(modelPosteRadio)
    controller.run()

if __name__ == '__main__':
    main()