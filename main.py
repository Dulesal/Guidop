from Controller.RadioController import RadioController
from Model.PosteRadio import PosteRadio
from Model.StationRadio import StationRadio
from View.PosteRadioView import PosteRadioView
from Model.Resistant import Resistant

def main():

    #Creation des resistants
    resistant1 = Resistant("Jean", "Les chants les plus désespérés sont les chants les plus beaux")
    resistant2 = Resistant("Patrick", "Message important pour Nestor: la girafe a un long cou")
    resistant3 = Resistant("Marcel", "Les carottes sont cuites")

    resistant = []
    resistant.append(resistant1)
    resistant.append(resistant2)
    resistant.append(resistant3)

    modelPosteRadio = PosteRadio("désespérés")
    viewPosteRadio = PosteRadioView()
    modelPosteRadio.addObserver(viewPosteRadio)

    modelStationRadio = StationRadio("BBC", resistant)

    controller = RadioController()
    controller.addStationRadio(modelStationRadio)
    controller.addPosteRadio(modelPosteRadio)
    controller.run()

if __name__ == '__main__':
    main()