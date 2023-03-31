## CLASS TREE
#extension de la classe BinTree �tous les types d'arbres
class Tree:
    """
    Classe Tree
    - Attributs :
        root : La racine root de type N (ou None)
        *children : les enfants de l'arbre du type Tree
        Un arbre vide est représenté par un objet dont la racine est None et aucun enfant n'est passé en arguments, c'est à dire qu'il y a au plus 1 argument
      
    - Condition : Un arbre est vide si et seulement si la racine est non définie
    
    - Méthodes(12) : 
        * Constructeur - Tree(racine, *children)
        * estVide()
        * estFeuille()
        * racine()
        * countOfChildren()
        * getChildren()
        * getChild()
        * setChild()
        * getEtage()
        * nodeInTree()
        * hauteur()
        * taille()
        * arite()
        * BFS()
        * DFS()

    """
    def __init__(self, root = None, *children):
        """
        CONSTRUCTOR        
        
        Parameters
        ----------
        root : not bool, value of the root. The default is None -> arbre vide.
        *children : children of the root -> instance of tree or None

        Create a Tree object
        -------
        CONSTRUCTOR

        """
        #Pré-conditions : tous les enfants doivent être des arbres
        for child in children :
            assert(isinstance(child, Tree) or child == None), f"{child} doit être un Tree ou None"
        
        self.root = root

        if len(children) == 0:
            self.children = []
        else:
            self.children = [child  for child in children]
        
        #Axiome
        assert self.estVide() == (self.root == None), "Un arbre non vide a une racine"
    
    
    ## Méthodes
    def estVide(self):
        """ Renvoie True si l'arbre est vide False sinon"""
        return (self.root == None) and (len(self.children) == 0)
    
    def estFeuille(self):
        return self.getChildren()[0].estVide() #un arbre ayant une feuille a au minimum un enfant
    
    def racine(self):
        return self.root
    
    def countOfChildren(self):
        """ renvoie le nbre d'enfants"""
        return len(self.children)
            
    def getChildren(self):
        if self.countOfChildren() != 0:
            return self.children
        else:
            return [Tree()] ##Renvoie un arbre vide si pas d'enfants
            
    def getChild(self, index):
        """ Renvoie le fils à l'indice indiqué """
        if not self.getChildren() == []: #Si il a des enfants
            if not(self.children[index].estVide()): #Si il il y a un enfant à l'endroit indiqué
                return self.children[index]
            else:
                return None
        
    def setChild(self, index, value):
        if not self.children[index].estVide():
            self.children[index] = value
    
    
    def getEtage(self, n:int)->list:
        """ Renvoie une liste des enfants de l'arbre à l'étage donné """
        if n == 0 :
            return self.racine()
        else:
            return [child.getEtage(n - 1) for child in self.getChildren()]
        
    def nodeInTree(self, node):
        
        assert type(node) is Tree or type(node) is not None, "L'objet en args doit être un arbre"
        if self.estVide():
            return False
        if (self.racine() == node.racine()) and (self.getChildren() == node.getChildren()):
            return True
        else:
            ListValues = [elt.nodeInTree() for elt in self.children]
            return (True in ListValues) 
        
    ## Mesures

    def hauteur(self):
        if self.estVide():
            return -1
        if self.estFeuille():
            return 0
        else:
            ListHauteurs = [elt.hauteur() for elt in self.children]
            return max(ListHauteurs) + 1
         
    def taille(self):
        """ Renvoie la taille de l'arbre"""
        if self.estVide():
            return 0
        else:
            listeTailles = [elt.taille() for elt in self.getChildren()]
            return 1 + sum(listeTailles)
        
    def arite(self):
        """ Renvoie l'arité de l'arbre (nbre d'enfants max)"""
        if self.estFeuille():
            return 0
        else:
            listArite = [elt.arite() for elt in self.getChildren()] #arite de chaque noeuds -> len(l) -> arite du noeud actuel
            return max(max(listArite), len(listArite))            
    
    ## Parcours
    def DFS(self):
        listeFinale = [] #Contiendra les valeurs qui montreront la manière dont le parcours est effectué
        pile = []
        pile.append(self)
        while len(pile) != 0:
            temp = pile.pop()
            listeFinale.append(temp.racine())
            for enfant in temp.getChildren():
                if not enfant.estVide():
                    pile.append(enfant)
        return listeFinale
    def BFS(self):
        listeFinale = []
        fileFIFO = []
        fileFIFO.insert(0, self)
        while len(fileFIFO) != 0:
            temp = fileFIFO.pop()
            listeFinale.append(temp.racine())
            for enfant in temp.getChildren():
                if not enfant.estVide():
                    fileFIFO.insert(0, enfant)
        return listeFinale
arbre = Tree(4, Tree(2, Tree(5),Tree(6),Tree(8), Tree(9), Tree(90)),Tree(12, Tree(25), Tree(32)), Tree(22,Tree(8, Tree(6), Tree(10, Tree(3))), Tree(56))) 
