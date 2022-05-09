import matplotlib.pyplot as plt
from function import colonneCouleur, ligneCouleur,tableauNoir,diagoCouleurVersBas,diagoCouleurVersHaut
from list_couleurs import vertClair,vertFonce,violet,rose,orange,jaune,bleu,blanc,noir,marron
def perroquet():
    """
    Retourne un perroquet
    -------
    
    """
    table = tableauNoir(26,35)#on commence par créer un tableau avec un fond noir
    
### Début de dessin, on commence par le haut de la tête

    ligneCouleur(7, 9, 8, vertFonce, table)
    ligneCouleur(8, 8, 10, vertFonce, table)
    ligneCouleur(9, 7, 12, violet, table)
    ligneCouleur(9, 10, 6, vertFonce, table)
    ligneCouleur(10, 7, 12, rose, table)
    ligneCouleur(11, 6, 14, rose, table)
    ligneCouleur(10, 11, 4, vertFonce, table)
    ligneCouleur(11, 11, 4, vertFonce, table)
    
    #Début de la crête du perroquet
    colonneCouleur(6,11,4,vertClair,table)
    colonneCouleur(6,12,6,vertClair,table)
    colonneCouleur(6,13,6,vertClair,table)
    colonneCouleur(6,14,4,vertClair,table)
    #Fin de la crête du perroquet
    
### Début du dessin des yeux

    #oeil gauche
    colonneCouleur(12, 7, 2, blanc, table)
    colonneCouleur(11, 8, 4, blanc, table)
    colonneCouleur(11, 9, 4, blanc, table)
    colonneCouleur(12, 10, 4, blanc, table)
    table[13][9] = noir # pupille gauche
    #oeil droit
    
    colonneCouleur(12, 15, 4, blanc, table)
    colonneCouleur(11, 16, 4, blanc, table)
    colonneCouleur(11, 17, 4, blanc, table)
    colonneCouleur(12, 18, 2, blanc, table)
    table[13][16] = noir # pupille droite
    
###Début des ailes, on les fait par souci pratique(superposition des lignes)
    
    ligneCouleur(18, 7, 12, jaune, table)
    ligneCouleur(19, 6, 14, bleu, table)
    ligneCouleur(19, 8, 10, jaune, table)
    ligneCouleur(20, 6, 14, bleu, table)
    ligneCouleur(21, 6, 14, bleu, table)
    ligneCouleur(22, 6, 14, bleu, table)
    ligneCouleur(23, 7, 12, bleu, table)
    
###Fin des ailes   
###Début des contours des yeux

    #contours orange a droite
    
    colonneCouleur(13, 19, 2, orange, table)
    colonneCouleur(14, 18, 3, orange, table)
    diagoCouleurVersHaut(17, 16, 2, orange, table)
    colonneCouleur(17, 15, 3, orange, table)
    
    #contours orange à gauche
    
    diagoCouleurVersBas(14, 6, 5, orange, table)
    colonneCouleur(17, 10, 3, orange, table)
    table[13][6] = orange
    table[16][7] = orange
    
    #contours rose à droite
    
    table[12][19] = rose
    diagoCouleurVersHaut(16, 16, 2, rose, table)
    ligneCouleur(16, 14, 3, rose, table)
    table[15][16] = rose
    
    #contours rose à gauche
    
    diagoCouleurVersBas(14, 7, 3, rose, table)
    diagoCouleurVersBas(15, 9, 2,rose, table)
    table[16][11] = rose
    table[12][6] = rose
    
### Fin de la partie haute du perroquet, comprenant la tête
### Début du buste du perroquet

    ligneCouleur(17, 11, 4, rose, table)
    ligneCouleur(18, 11, 4, rose, table)
    diagoCouleurVersHaut(22, 8, 4, violet, table)
    diagoCouleurVersBas(19, 14, 4, violet, table)
    diagoCouleurVersHaut(21, 10, 3, vertFonce, table)
    diagoCouleurVersBas(19, 13, 3, vertFonce, table)
    ligneCouleur(22, 10, 6, vertFonce, table)
    ligneCouleur(23, 10, 6, vertFonce, table)
    colonneCouleur(22, 9, 2, violet, table)
    colonneCouleur(22, 16, 2, violet, table)
    ligneCouleur(20,12,2,vertClair,table)
    ligneCouleur(21,11,4,vertClair,table)
    ligneCouleur(22,11,4,vertClair,table)
    ligneCouleur(23,11,4,vertClair,table)
    
###Fin du buste
###Début de la branche et de l'arbre sur lequel le perroquet se trouve
        
    table[23][8] = marron
    table[23][17] = marron
    ligneCouleur(23, 12, 2, marron, table)
    ligneCouleur(24, 0, 21, marron, table)
    ligneCouleur(25, 0, 21, marron, table)
    colonneCouleur(0, 0, 35, marron, table)
    colonneCouleur(0, 1, 35, marron, table)
    colonneCouleur(0, 2, 35, marron, table)
    diagoCouleurVersHaut(24,21,4,marron,table)
    diagoCouleurVersHaut(25,21,4,marron,table)
    diagoCouleurVersHaut(25,20,4,marron,table)
    diagoCouleurVersHaut(6, 0, 2, noir, table)
    ligneCouleur(20,23,3,vertClair,table)
    table[19][24] = vertClair
    table[7][1] = noir
    diagoCouleurVersHaut(5, 3, 4, marron, table)
    table[2][7] = marron
    ligneCouleur(1, 5, 4, vertClair, table)
    ligneCouleur(0, 6, 2, vertClair, table)
    
    
###Fin de la branche
###Début de la queue

    ligneCouleur(26, 10, 6, rose, table)
    ligneCouleur(27, 11, 4, rose, table)
    colonneCouleur(28, 12, 3, violet, table)
    colonneCouleur(28, 13, 3, violet, table)

    return(table)

### Lancement du programme ###

table = tableauNoir(24,35)
logo = perroquet()
plt.figure()
plt.axis('off') #On enleve le marquage des axes pour que ce soit plus joli
plt.title("Perroquet")
plt.imshow(logo)
plt.show()