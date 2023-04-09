from Tree import Tree #import de la classe Tree
import random
class Hydre(Tree):
    """
    Hercule à du affronter lors de son deuxieme travail l'Hydre de Lerne. 
    Cette hydre, à vous de l'affronter aujourd'hui !
    Pour la tuer il ne doit rester aucune tête, en êtes vous capables?
    Vous disposez de plusieurs méthodes pour tuer l'hydre:
        - Couper une tête : couper(tete)
        - Etat de l'hydre : etat()
        - Pour visualiser l'hydre : print()
        
    """
    def __init__(self, racine = None, *voisins):
        Tree.__init__(self, racine, voisins)
        
        self.nombreTetes = 9
        self.role = "utilisateur"
        self.nombreCoups = 0
        

    def testVictoire(self):
        """ Renvoie True si l'hydre n'a plus de têtes (si elle morte ...) """
        for child in self.getChildren():
            if not child.estVide():
                return False
        return True
            
    def victoire(self):
        """ Renvoie un message de victoire """
        return "Bravo vous avez battu l'Hydre !!!!"
        
            
    def couper(self, tete):
        if not self.nodeInTree(tete):
            listeCorps = ["à la tête",
                          "au pied",
                          "à la cheville",
                          "au talon, Vous avez de la chance que je ne sois pas achille",
                          "à la jambe",
                          "au bras",
                          "au torse"]
            endroit = listeCorps[random.randint(0, len(listeCorps))]
            return f"Vous devez couper un membre de l'Hydre, vous venez de me faire mal {endroit} !!"
        #si le joueur est hercule il n'a pas besoin de faire d'effort et gagne directement
        if self.role == "Hercule": # Si le role du joueur est hercule
            self.nbreTetes = 0
            self.etat = "dead"
            return self
        ## Si la tete est rattaché au corps, alors elle est coupée définitivement
        if tete.parent().racine() == self.racine():
            for i in range(len(self.getChildren())):
                if self.getChildren()[i] == tete:
                    self.setChild(Hydre(), i)
        ## Si la tete n'est pas directemnt relié au corps il en repousse plusieurs
        else:

            #il faut d'abord supprimer le noeud donné par l'user
            tempHydre = self.parent(tete)
            tempHydre.delChild(tete)
            self.nbreTetes -= 1
            #On récupère le nbre de tetes sur la branche qu'on vient de couper
            nbreEnfants = len(tempHydre.getChildren())
            #Ensuite on récupère la branche de la tête donnée
            while self.parent(tempHydre).racine() != self.racine():
                tempHydre = self.parent(tempHydre)

            #On récupére l'indice de la branche à modifier et on modifie l'arbre
            indice = 0 
            while tempHydre.racine() != self.getChildrenRacines()[indice]:
                indice += 1
            self.setChild(tempHydre, indice)

            #Il faut maintenant faire repousser n fois le nbre de branche qu'on vient de couper
            self.nombreCoups += 1 #On a mis un coup à l'hydre pr couper la tête -> coups incrémente
            for i in range(self.nombreCoups):
                self.setChild(tempHydre) #Ajout aux enfant de la branche
                self.nbreTetes += nbreEnfants #ajout du nombre de tetes qu'on rajoute aux nombre de tetes totales
            #Arbre.renommer() créer une méthode pour renommer tous les noeuds de l'arbre
        
        def renommer(self):
            index = 1
            pile = []
            pile.append(self)
            while len(pile) != 0:
                if pile[-1].estFeuille(): #si c'est une feuille on renomme avec le numéro de tête
                    pile[-1].setRacine(f"Tête {index}") 
                    index += 1
                else:
                    pile[-1].setRacine(f"cou") #si c'est autre chose qu'une feuille, c'est un cou ou la racine -> on etudiera le dernier cas + tard
                for enfant in pile[-1].pop().getChildren(): #parcours dfs
                    if not enfant.estVide():
                        pile.append(enfant)
            self.setRacine("corps") #on gére le cas de la racine, cette derniere prendra la valuer 'cou' or c'est le corps de l'hydre
    
    def devenirHercule(self):
        self.role = "Hercule"
        print("Vous avez reçu un arc et une massue.")
        return None


