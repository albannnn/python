def tableauNoir(lignes,colonnes):
    """


    Parameters
    ----------
    x : int, nombre de lignes du tableau voulu
    y : int, nombre de colonnes du tableau voulu

    Retourne le tableau avec x lignes et y colonnes, de couleur noir
    -------

    """
    table = [[0 for x in range(lignes)] for y in range(colonnes)] #création d'un tableau avec le nombre de lignes et de colonnes indiquées par l'utilisateur
    for x in range(lignes):     #on parcours toutes les lignes et toutes les colonnes
        for y in range(colonnes):
            table[y][x] = [0,0,0] # on les mets a 0,0,0, couleur noire
    return(table)

def ligneCouleur(ligne,colonne, nombrePixels, couleur,table):

    """

    Parameters
    ----------
    ligne : int, numéro de la ligne où le changement de couleur est voulu
    colonne: int, numéro de la colonne où le changement est voulu
    nombrePixels : int, nombre de pixels sur lesquels vont s'appliquer la couleur
    couleur : list, pixel de couleur r-g-b

    créé une ligne d'un nombre de pixels déterminés en argument, de couleur et à la position aussi determinée en arguments
    -------

    """

    for y in range(0,nombrePixels):     #On parcours la liste pendant le nombre de pixels mis en arguments
        table[ligne][colonne] = couleur # Changement de la couleur aux coordonnées indiquées
        colonne = colonne + 1 #on ajoute 1 a la colonne pour que le prochain pixel se décale d'une colonne
    return(table)


def colonneCouleur(ligne,colonne, nombrePixels, couleur,table):

    """

    Parameters
    ----------
    ligne : int, numéro de la ligne où le changement de couleur est voulu
    colonne: int, numéro de la colonne où le changement est voulu
    nombrePixels : int, nombre de pixels sur lesquels vont s'appliquer la couleur
    couleur : list, pixel de couleur r-g-b

    créé une ligne d'un nombre de pixels déterminés en argument, de couleur et a la position aussi determinée en arguments
    -------

    """

    for y in range(0,nombrePixels): #Pour le nombre de pixels donnés
        table[ligne][colonne] = couleur#On change la couleur avec la couleur données en arguments
        ligne = ligne + 1 #on ajoute 1 a la ligne pour que le prochain pixel se décale d'une case vers le bas
    return(table)

def diagoCouleurVersBas(ligne,colonne,nombrePixels,couleur,table):
    """

    Parameters
    ----------
    ligne : int, n°de la ligne ou on veut que commence la diagonale
    colonne : int, n° de la colonne ou on veut que ommence la diagonale
    nombrePixels: int, nombre de pixels que la diagonale va faire
    couleur: list, list de la forme r-g-b, qui donne la couleur à la diagonale
    table: list, tableau dans lesule on veut placer la diagonale

    créé une diagonale descendante du nombre de pixels demandés, de couleur et à la position aussi determinée en arguments
    """
    
    for y in range(0, nombrePixels):
        table[ligne][colonne] = couleur
        colonne = colonne + 1
        ligne = ligne + 1
    return(table)

def diagoCouleurVersHaut(ligne,colonne,nombrePixels,couleur,table):
    """

    Parameters
    ----------
    ligne : int, n°de la ligne ou on veut que commence la diagonale
    colonne : int, n° de la colonne ou on veut que ommence la diagonale
    nombrePixels: int, nombre de pixels que la diagonale va faire
    couleur: list, list de la forme r-g-b, qui donne la couleur à la diagonale
    table: list, tableau dans lesule on veut placer la diagonale

    créé une diagonale montante du nombre de pixels demandés, de couleur et à la position aussi determinée en arguments
    """
    
    for y in range(0, nombrePixels):
        table[ligne][colonne] = couleur
        colonne = colonne + 1
        ligne = ligne - 1
    return(table)

