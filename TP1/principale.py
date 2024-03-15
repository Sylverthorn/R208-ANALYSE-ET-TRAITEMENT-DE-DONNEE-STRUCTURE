from voiture import *

if __name__ == "__main__":

    mycar1 = Voiture("toyota", "M3", 3, "jaune")
    mycar2 = Voiture()
    mycar3 = Voiture("tesla", "S", 6)
    mycar4 = Voiture(couleur="Noire")
    
    
    mycar1.set_couleur("bleu")
    mycar1.set_option("siege chauffant")
    mycar1.set_option("barbecue")


    
    print(mycar1)
    print(mycar2)
    print(mycar3)
    print(mycar4)
