from Tree import Tree #import de la classe Tree
import random
class Hydre(Tree):
    """
    Hercule à du affronter lors de son deuxieme travail l'Hydre de Lerne. 
    Cette hydre, à vous de l'affronter aujourd'hui !
    Pour la tuer il ne doit rester aucune tête, en êtes vous capables?
    Vous disposez de plusieurs méthodes pour tuer l'hydre:
        - Couper une tête : couper(tete), dans le cas où la branche contient plusieurs têtes -> elles repoussent toutes
        - abandonner()
        -état de l'hydre : etat()
        -visualiser l'hydre : visualiser()
        *** cachée *** -> devenir Hercule
    """
    def __init__(self, racine = None, *voisins):
        Tree.__init__(self, racine, voisins)
        self.etat = "alive"
        self.nbreTetes = 9
        self.role = "utilisateur"
        self.coupEpee = 0
    
    def victoire(self):
        return "Bravo vous avez battu l'Hydre !!!!"

    def parent(self, node):
        """ Retourne le parent du noeud en args si il est dans l'arbre False sinon ou si c'est la racine de l'arbre"""
        if not self.nodeInTree(node): #Si le noeud n'est pas dans l'arbre, alors il ne peut avoir de parents
            return False
        if self.racine() == node.racine() or self.estFeuille(): 
            return False
        listeNodes = [nodeFromList for nodeFromList in self.getChildren()] #récupération de tous les enfants du neouds principal
        if node in listeNodes: #Si le noeud recherché est dans la liste d'enfant, alors on est bien le noeud parent 
            return self
        else:
            for nodeFromList in listeNodes: #Parcours de la liste contenant les noeuds
                temp = nodeFromList.parent(node) #Appel récursif
                if not temp:   
                    return temp
        #A TESTER
        
            
    def couper(self, tete):
        if self.role == "Hercule":
            self.nbreTetes = 0
            self.etat = "dead"
            print(self.victoire())
            return self
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
        
    def devenirHercule(self):
        self.role = "Hercule"
        print("Vous avez reçu une vrai épée et une armure bénie des Dieux.")
        return None

