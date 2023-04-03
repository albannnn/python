# CLASS TREE
# extension de la classe BinTree �tous les types d'arbres
class Tree:
    """
    Classe Tree
    - Attributs :
        root : La racine root de type N (ou None)
        *children : les enfants de l'arbre du type Tree
        Un arbre vide est représenté par un objet dont la racine est None et aucun enfant n'est passé en arguments, c'est à dire qu'il y a au plus 1 argument
      
    - Condition : Un arbre est vide si et seulement si la racine est non définie
    
    - Méthodes(18) : 
        * Constructeur - Tree(racine, *children)
        * estVide()
        * estFeuille()
        * racine()
        * countOfChildren()
        * getChildren()
        * getChild()
        * setChild()
        * delChild()
        * setRacine()
        * getEtage()
        * nodeInTree()
        * hauteur()
        * taille()
        * arite()
        * BFS()
        * DFS()
        * __str__()

    """

    def __init__(self, root=None, *children):
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
        
        # Pré-condition : tous les enfants doivent être des arbres
        for child in children:
            assert (isinstance(child, Tree) or child ==
                    None), f"{child} doit être un Tree ou None"
        # Pré-condition : Une valeur ne peut se trouver 2 fois dans l'arbre
        assert not self.nodeInTree(self), "Un noeud ne peut se trouver qu'une seule fois dans l'arbre"
        
        self.root = root

        if len(children) == 0:
            self.children = []
        else:
            self.children = [child for child in children]

        # Axiome
        assert self.estVide() == (self.root == None), "Un arbre non vide a une racine"
    #Redéfinition de la superiorité -> relation d'ordre des arbres
    ##A FAIRE
    # Impression
    def __str__(self, level=0):
        """ Représentation de l'arbre """
        if self.estVide():
            return ''
        result = ''
        result += '  ' * level + '|' + str(self.racine()) + '\n'
        for child in self.getChildren():
            result += child.__str__(level+1)
        return result

    # Méthodes
    def estVide(self):
        """ Renvoie True si l'arbre est vide False sinon"""
        return (self.root == None) and (len(self.children) == 0)

    def estFeuille(self):
        """ Renvoie True si l'arbre est une feuille False sinon (un arbre ne contenant qu'un seul noeud est une feuille)"""
        return self.getChildren()[0].estVide()  # un arbre ayant une feuille a au minimum un enfant

    def racine(self):
        """ Renvoie la valeur de la racine"""
        return self.root

    def countOfChildren(self):
        """ renvoie le nombre d'enfants"""
        return len(self.children)

    def getChildren(self):
        """ Renvoie la liste des enfants si il y en a, un arbre vide sinon"""
        if self.countOfChildren() != 0:
            return self.children
        else:
            return [Tree()]  # Renvoie un arbre vide si pas d'enfants

    def getChild(self, index):
        """ Renvoie le fils à l'indice indiqué """
        if not self.getChildren() == []:  # Si il a des enfants
            # Si il il y a un enfant à l'endroit indiqué
            if not (self.children[index].estVide()):
                return self.children[index]
            else:
                return None

    def setChild(self, value):
        """ Ne renvoie rien, change la valeur d'un enfant de l'arbre"""
        self.children.append(value)

    def delChild(self, delete):
        """ Supprime un enfant de l'arbre passé en args"""
        assert self.nodeInTree(delete), "Pour supprimer un enfant, il doit être dans l'arbre"
        for i in range(len(children := self.getChildren())):
            if children[i] == delete:
                children[i] == Tree
        
    def setRacine(self, value):
        """ Change la valeur de la racine, Ne renvoie rien"""
        self.root = value

    def getEtage(self, n: int) -> list:
        """ Renvoie une liste des enfants de l'arbre à l'étage donné """
        if n == 0:
            return self.racine()
        else:
            return [child.getEtage(n - 1) for child in self.getChildren()]

    def nodeInTree(self, node):
        """ Renvoie True si `node` est dans l'arbre False sinon"""
        assert type(node) is Tree or type(
            node) is not None, "L'objet en args doit être un arbre"
        if self.estVide():
            return False
        if (self.racine() == node.racine()):
            return True
        else:
            ListValues = [elt.nodeInTree(node) for elt in self.children]
            return (True in ListValues)

    # Mesures

    def hauteur(self):
        """ Renvoie la hauteur de l'arbre """
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
            # arite de chaque noeuds -> len(l) -> arite du noeud actuel
            listArite = [elt.arite() for elt in self.getChildren()]
            return max(max(listArite), len(listArite))

    # Parcours
    def DFS(self):
        """ Renvoie une liste du parcours en profondeur de l'arbre `Depth First Search` """
        listeFinale = []  # Contiendra les valeurs qui montreront la manière dont le parcours est effectué
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
        """ Renvoie une liste du parcours en largeur de l'arbre `Breadth First Search` """
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


# Exemple d'arbre
arbre = Tree(4, Tree(2, Tree(5), Tree(6), Tree(8), Tree(9), Tree(90)), Tree(
    12, Tree(25), Tree(32)), Tree(22, Tree(8, Tree(6), Tree(10, Tree(3))), Tree(56)))
#print(arbre)

