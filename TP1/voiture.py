
class Voiture:

    def __init__(self, marque="BMW", modèle="X", puissance_fiscale="0", couleur="Blanche"):
        self.__modèle = modèle
        self.__marque = marque
        self.__puissance_fiscale = puissance_fiscale
        self.__couleur = couleur
        self.__option = []
    
    def get_marque(self):
        return self.__marque
    
    def get_modèle(self):
        return self.__modèle
    
    def get_puissance_fiscale(self):
        return self.__puissance_fiscale
    
    def get_couleur(self):
        return self.__couleur
    
    def get_option(self):
        return self.__option

    def set_marque(self , value):
        self.__marque = value

    def set_modèle(self , value):
        self.__modèle = value

    def set_puissance_fiscale(self , value):
        self.__puissance_fiscale = value

    def set_couleur(self , value):
        self.__couleur = value

    def set_option(self, value):
        self.__option.append(value)

    def remove_option(self, option):
        self.__option.remove(option)


    
    def __str__(self):
        return f"""----------------------------\n
- marque            : {self.__marque}
- modèle            : {self.__modèle}
- puissance fiscale : {self.__puissance_fiscale}
- couleur           : {self.__couleur}
- option            : {self.__option}\n"""
    
