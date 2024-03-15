from forme import *


if __name__ == "__main__":
    #rectangle1 = Rectangle()
    #rectangle1.set_widht()
    #rectangle1.set_height()

    #rectangle1.get_area()
    #rectangle1.get_picture()
    #print(rectangle1)


    #rectangle1.get_amount_inside()

    i = 0
    sq = Carre()
    while i < 51:
        if i == 50 :
            i = 0
        sq.side(i)
        sq.get_picture()
        i += 1
    print(sq.__dict__)