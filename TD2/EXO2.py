import sys

def main():
    if len(sys.argv)>=2:
        filename=sys.argv[1]
        fichier = open(filename, 'r')
    for ligne in fichier:
        ligne = ligne.rstip("\r\n")
        print(ligne)    

if __name__ == "__main__":
    main()


