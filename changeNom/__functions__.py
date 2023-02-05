# @albannnn on Github
## IMPORT

import os

##FONCTIONS

def __main__(path,car:list, n = 0):
        assert os.path.exists(path) == True, 'Vous devez utiliser un chemin présent sur votre ordinateur'

        os.chdir(path) #On va dans le repertoire où sont les fichiers
        liste = os.listdir()
        for fichier in liste:
            if(fichier != f"ticket {str(n)}.{__typeOf__(fichier)}") and (not __carInFile__(fichier, car)) and not(__isDir__(fichier)) : # condition si le ticket existe deja et si la chaine n'est pas dans le fichier
                os.rename(fichier, f"ticket{n}.{__typeOf__(fichier)}") #nom du nouveau fichier
                n += 1
            if __isDir__(fichier):
                    __main__(path + f"/{fichier}", car ,n)


def __isDir__(file:str, n = -1): #recursive fonc
    """
    Entrée : file : str : Fichier a tester
    Renvoie True si le fichier testé est un répertoire False sinon
    """
    if abs(n) == len(file): #Si on a parcouru tout le fichier
        return True

    if file[n] == '.': #Le fichier n'est pas un répertoire ssi il y a un point dans son nom
        return False
    else:
        return __isDir__(file, n - 1) #On répéte la fonction à partir de la lettre qui précéde


def __carInFile__(file, listCar):
    """
    Test si  une ou plusieurs chaine de caractères est/sont dans le fichier
    """

    for val in listCar:
        if val in file:
            return True
    return False



def __typeOf__(file:str):
    """
    Entrée : str : nom de fichier
    Renvoie l'extension du fichier

    -------

    Exemple:
    __typeOf__("fichierTest.php")
    >>> 'php'
    """
    try :
        carFinale = ""
        i = -1
        while file[i] != ".":
            carFinale = file[i]  + carFinale
            i -= 1
        return carFinale
    except IndexError:
        print("C'est un répertoire!")
