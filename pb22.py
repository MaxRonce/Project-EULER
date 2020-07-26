#Cette fonction prend en paramètre un nom/mot et retourne sa valeur alphabétique
def name_score(name):
    score = 0
    #Lecture un par un des lettres du mot
    for i in name:
        #La fonction ord prend en paramètre un caractère et retourne son code ascii
        #Le code ascii de A étant 65, il nous faut soustraire 64 au code ascii
        #d'une lettre pour obtenir sa position dans l'alphabet
        score += ord(i) - 64
    return score

fichier = open("C:\Users\maxro\Desktop\ProjectEuler-master\p022_names.txt.txt", "r")
#Lecture des noms du fichier et génération de la liste des noms
names = list(eval(fichier.read()))
fichier.close()
names.sort()
resultat = 0
for i, name in enumerate(names):
    resultat += name_score(name)*(i+1)
print(resultat)