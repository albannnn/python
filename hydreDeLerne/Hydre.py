from Tree import Tree #import de la classe Tree
import random
class Hydre(Tree):
    """
    Hercule à du affronter lors du deuxieme de ses douzes travaux l'Hydre de Lerne. 
    Cette hydre, à vous de l'affronter aujourd'hui !
    Pour la tuer il ne doit rester aucune tête, en êtes vous capables?
    Vous disposez de plusieurs méthodes pour tuer l'hydre:
        - Couper une tête : couper(tete)
        - Etat de l'hydre : etat()
        - Pour visualiser l'hydre : print()
        
    """
    
    def __init__(self, racine = None, *children):
        Tree.__init__(self, racine, *children)
        
        self.nombreTetes = 9
        self.role = "utilisateur"
        self.nombreCoups = 0
    def __repr__(self):
        return f"<Hydre object root = {self.racine()}>"
    
    
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
            
            endroit = random.choice(listeCorps)
            print(f"Vous devez couper un membre de l'Hydre, vous venez de me faire mal {endroit} !!")
            return None
        #si le joueur est hercule il n'a pas besoin de faire d'effort et gagne directement
        if self.role == "Hercule": # Si le role du joueur est hercule
            self.nbreTetes = 0
            self.etat = "dead"
            self = Hydre()
            print(self.victoire())
            return self
        if not tete.estFeuille():
            print("Vous devez couper une tête !!!")
            return None
        # Si la tete est la racine de l'arbre -> on ne peut pas la couper
        if tete.racine() == self.racine():
            print("Vous ne pouvez pas couper le corps de l'hydre")
            return None
        # Si la tete est rattaché au corps, alors elle est coupée définitivement
        if self.parent(tete).racine() == self.racine():
            for i in range(len(self.getChildren())):
                if self.getChildren()[i] == tete:
                    self.setChild(Hydre(), i)
                    self.nombreCoups += 1
        ## Si la tete n'est pas directemnt relié au corps il en repousse plusieurs
        else:

            #il faut d'abord supprimer le noeud donné par l'user
            tempHydre = self.parent(tete)
            tempHydre.delChild(tete)
            self.nombreTetes -= 1
            #On prend ensuite le noeud qui précéde le parent du noeud coupé, c'est à ce noeud que la tête va repousser
            tempHydre = self.parent(tempHydre)
            #La tete qu'on vient de couper va repousser n fois à partir du noeud précédent
            self.nombreCoups += 1 
            for i in range(self.nombreCoups):
                tempHydre.setChild(Hydre('nouveau'), 'append') 
                self.nombreTetes += 1 

            
        self.rename()
        
    def rename(self):
        """ Renommage de l'hydre """
        index = 1
        pile = []
        pile.append(self)
        while len(pile) != 0:
            if pile[-1].estFeuille(): #si c'est une feuille on renomme avec le numéro de tête
                pile[-1].setRacine(f"Tête {index}") 
                index += 1
            else:
                pile[-1].setRacine(f"cou") #si c'est autre chose qu'une feuille, c'est un cou ou la racine -> on etudiera le dernier cas + tard
            for enfant in pile.pop().getChildren(): #parcours dfs
                if not enfant.estVide():
                    pile.append(enfant)
        self.setRacine("corps") #on gére le cas de la racine, cette derniere prendra la valuer 'cou' or c'est le corps de l'hydre
    
    def devenirHercule(self):
        self.role = "Hercule"
        print("Vous avez reçu un arc et une massue.")
        return None
    

    

tree = Tree(4)
hydre = Hydre(1, 
              Hydre(2, Hydre(3), Hydre(4), Hydre(5), Hydre(6), Hydre(7)), 
              Hydre(8, Hydre(9), Hydre(10)), 
              Hydre(11, Hydre(12, Hydre(13), Hydre(14, Hydre(15))), Hydre(16)),
              Hydre(17))
print(hydre.parent(Hydre(5)))
print(hydre.getEtage(2))
print(hydre.nodeInTree(Hydre(22, Hydre(88), Hydre(56))))
#print(hydre.nodeInTree(Hydre(5)))

print(Hydre(5) in hydre.getEtage(2))
a = Hydre(5)
b = Hydre(5, Hydre(2))
hydre.rename()
print(hydre)
toCut = Hydre(input("Quelle tête ? : "))
hydre.couper(toCut)
print(hydre)
hydre.devenirHercule()
toCut = Hydre(input("Quelle tête ? (2) :"))
print(hydre)
