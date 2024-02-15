import subprocess
def add_user_to_group():
    username = input("Indiquez le nom de l'utilisateur à ajouter à ungroupe: ")
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]
    print("Entrez une liste de groupes auxquels ajouter l'utilisateur")
    print("La liste doit être séparée par des espaces, par exemple:\r\n group1 group2 groupe3")
    print("Les groupes disponibles sont :\r\n " + output)
    chosenGroups = str(input("Groups: "))