
def divEuclidienne(a,b):
    """ Renvoie la division Euclidienne de a par b sous la forme d'un tuple (signe //)"""
    ##UNIQUEMENT DES NVRES POSITIFS PR L'INSTANT
    assert b != 0, 'On ne peut pas diviser un nombre par 0'
    if (a >= 0 and b > 0) or (a <= 0 and b < 0): #si les 2 nombres ont le meme signe pas de problemes
        if b > a:
            return 0
        else:
            return 1 + divEuclidienne(a - b, b)
    else: 
        if b < a :
            ##WIP
            return None


def modulo(a,b):
    """ renvoie le reste de la division euclidienne de a par b(signe %)"""
    return a - b * divEuclidienne(a,b)
    
    
def diviseurs(n):
    """ Renvoie la liste des diviseurs de n"""
    div = []
    for i in range(n):
        if n % i == 0:
            div.append(n)
    return [-elt for elt in div] + div #Pour avoir les diviseurs négatifs et positifs

def congru(a,b, mod):
    return modulo(a, mod) == modulo(b, mod)


## Programme principal
a = 13
b = 16
print(divEuclidienne(24,16))
print(congru(a,b, 3))
#print(Arithmetique.congru(a,b, 24))
