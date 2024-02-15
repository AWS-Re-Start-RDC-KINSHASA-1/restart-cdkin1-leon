import os
def install_or_remove_packages():
    iOrR = ""
    while iOrR != "I" and iOrR != "R":
        print("Vous souhaitez installer ou supprimer des packages? (I/R)")
        iOrR = input().upper()
    if iOrR == "I":
        iOrR = "install"
    elif iOrR == "R":
        iOrR = "remove"
    
    print("Entrez une liste de packages à installer")
    print("La liste doit être séparée par des espaces, par exemple :")
    print(" package1 package2 package3")
    print("Autrement, entrer 'default' dans " + iOrR + " les packages par défaut listés dans le programme")
    packages = input().lower()
    if packages == "default":
        packages = defaultPackages
    if iOrR == "install":
        os.system("sudo apt-get install " + packages)

    elif iOrR == "remove":
        while True:
            print("Purger les fichiers après la suppression? (Y/N)")
            choice = input().upper()
            if choice == "Y":
                os.system("sudo apt-get --purge " + iOrR + " " + packages)
                break
            elif choice == "N":
                os.system("sudo apt-get " + iOrR + " " + packages)
                break
        os.system("sudo apt autoremove")

def clean_environment():
    os.system("sudo apt-get autoremove")
    os.system("sudo apt-get autoclean")

def update_environment():
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")
    os.system("sudo apt-get dist-upgrade")
