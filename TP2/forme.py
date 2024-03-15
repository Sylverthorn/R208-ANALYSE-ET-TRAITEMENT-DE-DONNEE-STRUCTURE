class Rectangle:
    

    def __init__(self, widht=0, height=0) :
        self.__widht = widht
        self.__height = height

   
#SET HEIGHT AND WIDHT
    def set_widht(self, a = "None"):
        if a == "None":
            a = int(input("ENTREZ LA LARGEUR DU RECTANGLE : "))
        else:
            while a < 0:
                print ( "!! ERROR : valeur entré est négative ")
                a = int(input("entrez la largeur du rectangle : "))
        self.__widht =  a


    def set_height(self, a = None):
        if a == None:
            a = int(input("ENTREZ LA HAUTEUR DU RECTANGLE : "))
        else:
            while a < 0:
                print ( "!! ERROR : valeur entré est négative ")
                a = int(input("entrez la largeur du rectangle : "))
        self.__height =  a




# AFFICHAGE
    def __str__(self):
        return  f"Rectangle(widht = {self.__widht}, height= {self.__height})"  
    





# GET ALL
    def get_area(self):
        area = self.__widht * self.__height
        print(f"|¤| la surface est de : {area} ")
        return area


    def get_perimeter(self):
        perimeter = 2* (self.__height + self.__widht)
        print(f"|¤| le perimetre est de : {perimeter} ")


    def get_diagonal(self):
        diag = ((self.__widht ** 2 + self.__height ** 2) ** .5)
        print(f"|¤| la diagonale est de : {diag} ")
    

    def get_picture(self):
        if self.__height > 50 or self.__widht > 50 :
            print ("!! ERROR : Trop grand pour faire une image")
        else:
            print("\n"+ self.__widht * "* " + "\n" + (self.__height - 2)*("* " + (self.__widht - 2) * "  " + "*\n" ) + self.__widht * "* " + "\n")


    def get_amount_inside(self):
        larg = int(input("largeur : "))
        haut = int(input("hauteur : "))

        if haut == larg:
            form = "carré"
        else:
            form = "rectangle"

        ar = larg * haut
        b = self.get_area() // ar
        print(f"le {form} de largeur: {larg} et hauteur: {haut} peut tenir {b} fois dans le rectangle de largeur: {self.__widht} et hauteur: {self.__height} ")


class Carre(Rectangle):

    def __init__(self, widht= 0, height= 0, side = 0):
        super().__init__(widht, height)
        self.__side = side

    def set_side(self, a):
        self.set_widht(a)
        self.set_height(a)
        self.__side = a

  
    def side(self, a):
        self.set_side(a)


    def __str__(self):
        return f"Carre( side= {self.side})"
        