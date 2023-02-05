# @albannnn on Github
import os
from ticket import __main__ , __isRep__ , __carInFile__ , __typeOf__
## VARIABLES

path = "" #TODO mettre le chemin du premier répertoire
listNoChange = [] #TODO liste des chaines de caractères apparaissant dans les fichiers dont on ne veux pas changer le nom

##

"""
!!! ATTENTION !!!

Le programme n'est appliquable qu'une seule fois sur un même repertoire, il y aura erreur si il est éxécuté plusieurs fois sur les mêmes fichiers.
L'erreur sera : FileNotFoundError: [WinError 2] Le fichier spécifié est introuvable: 'ticket0.odt' -> 'ticket0.odt'

"""

#__main__(path, listNochange)