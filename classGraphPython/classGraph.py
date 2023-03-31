class Node:
    def __init__(self, value = None, voisins:list = []):
        """constructor"""
        self.value = value
        self.voisins = voisins
        
        assert self.estVide() == (self.value == None) 
        if self.estVide() and len(self.voisins != 0):
            raise ValueError("Un noeud vide n'a pas de voisins  ")