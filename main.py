from Controller.RadioController import RadioController
from Model.PosteRadio import PosteRadio
from Model.StationRadio import StationRadio
from View.PosteRadioView import PosteRadioView


def main():
    paroles = "Les sanglots longs des violons de l'automne blessent mon cœur d'une langueur monotone. Tout suffocant et blême, quand sonne l'heure, je me souviens des jours anciens et je pleure."
    print("Main function")
    modelPosteRadio = PosteRadio()
    modelStationRadio = StationRadio("BBC", paroles)
    controller = RadioController()
    viewPosteRadio = PosteRadioView()



if __name__ == '__main__':
    main()