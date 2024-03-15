
class Film :

    def __init__(self, titre = "0", date = "O" , note = 0, avis = []):
        self.__titre = titre
        self.__date = date
        self.__note = note
        self.__avis = avis
    
    def set_film(self):
        a = "O"
        self.__titre = input("ENTREZ LE TITRE DU FILM : ")
        self.__date = input("ENTREZ LA DATE DU FILM : ")
        self.__note = float(input("ENTREZ LA NOTE DU FILM : "))
        while a != "end!":
            a = input("ENTREZ LES AVIS : ")
            self.__avis.append("-" + a)
    
    def __str__(self):
        for i in self.__avis:
            a = 
        return f"""le film {self.__titre} est sortie en {self.__date}, il a la note {self.__note} et
voici les avis du public l'ayant vu :
{}
"""
        
      




class Bibliothèque:

    def __init__(self, liste_film):
        self.__liste_film = liste_film




