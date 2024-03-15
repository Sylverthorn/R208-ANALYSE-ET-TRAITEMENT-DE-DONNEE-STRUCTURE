import sys
import os

def affiche(dossier):
    for i in os.listdir(dossier):
        print (f"{i} \n")
def help(dir):
    print(f"Le répertoire {dir} n'existe pas...")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            affiche(sys.argv[1])

        else:
            help(sys.argv[1])


    else:
        print("pas d'arguments")
