
def somme_carre(num = 101):
    resultat = 0
    for i in range(1, num):
        temp  = i*i
        resultat = resultat + temp
        i += 1
    return resultat

def carre_somme(num = 101):
    resultat = 0
    for i in range(1, num):
        temp = i
        resultat = temp + resultat
    resultat = resultat * resultat
    return resultat

i = carre_somme() - somme_carre()

print(i)