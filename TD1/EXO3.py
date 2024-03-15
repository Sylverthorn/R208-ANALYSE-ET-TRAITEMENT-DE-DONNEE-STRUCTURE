import sys
import os

listeFichiers = ["FICHIERS", ""]
listeDossiers = ["DOSSIERS",""]


def recherche(dir):
    for i in os.listdir(dir):
        chemin = os.path.join(dir, i)
        if os.path.isfile(chemin):
            listeFichiers.append(chemin)
        elif os.path.isdir(chemin):
            listeDossiers.append(chemin)
    

def help(dir):
    print(f"Le répertoire {dir} n'existe pas...")

def résultat(list1, list2):
    for k in list1:
        print(k)
        
    print("""

    ----------------------------------------------------------------

        """)
    for n in list2:
        print(n)
    

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        recherche(sys.argv[1])
        résultat(listeFichiers, listeDossiers)
    else:
        help(sys.argv[1])


else:
    print("pas d'arguments")

