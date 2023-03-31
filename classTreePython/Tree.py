## CLASS TREE
#extension de la classe BinTree �tous les types d'arbres
class Tree:
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
        
    def arite(self):
        """ Renvoie l'arité de l'arbre (nbre d'enfants max)"""
        if self.hauteur() == 1:
            return self.countOfChildren()
        else:
            ListArite = [elt.arite() for elt in self.getChildren()]  
            return max(ListArite)      
    
    def ariteNoeud(self, node):
        """ Renvoie l'arite d'1 noeud (enfants du noeuds)"""

        return len(node.children)
    ## Parcours
arbre = Tree(4, Tree(2, Tree(5),Tree(6),Tree(8), Tree(9)), Tree(22,Tree(8, Tree(6), Tree(10, Tree(3))), Tree(56)))
print(arbre.arite())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    