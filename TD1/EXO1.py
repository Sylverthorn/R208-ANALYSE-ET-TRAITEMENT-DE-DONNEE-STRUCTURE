import sys

if __name__ == '__main__':

    if len(sys.argv) > 1:
        for i in sys.argv:
            print(i)
    else:
        print(f"Pas assez d’arguments pour le script {__name__}")