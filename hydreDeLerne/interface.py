from xml.dom.NodeFilter import NodeFilter
from createHydre import createHydre
from Hydre import Hydre
import random
import pygame 
import os



class Game:
    
    def __init__(self):
        pygame.init() #initialisation du module pygame entier

        #chemin du jeu dans l'ordi de l'utilisateur
        self.path = os.getcwd() + "\\"

        #attributs d'etats 
        self.running = True
        self.outOfStart = False
        self.gameEnd = False
        

        #fonts
        self.titleFont = pygame.font.Font(self.path + "HydreDeLerne\\font\\Lazer84.ttf", 140)
        self.textFontBold30 = pygame.font.Font(self.path + "HydreDeLerne\\font\\DejaVuSansMono-Bold.ttf", 30)
        self.textFontBold15 = pygame.font.Font(self.path + "HydreDeLerne\\font\\DejaVuSansMono-Bold.ttf", 15)
        self.textFont30 = pygame.font.Font(self.path + "HydreDeLerne\\font\\DejavuSansMono.ttf", 30)
        self.textFont15 = pygame.font.Font(self.path + "HydreDeLerne\\font\\DejavuSansMono.ttf", 15)

        #fps 
        self.clock = pygame.time.Clock()
        
        #icone et page
        self.icon = pygame.image.load(self.path + "\\HydreDelErne\\images\\TeteYellow.jpg")
        pygame.display.set_icon(self.icon)
        
        #attributs liés aux dimensions
        self.sizeX = 1280
        self.sizeY = 720
        self.screen = pygame.display.set_mode((self.sizeX, self.sizeY))

        #infos du jeu
        self.colors = {
            'purple':'#A458E3',
            'pink' : '#F056A1',
            'yellow' : '#FDE63B',
            'blue' : '#01A7F3', 
            'cyan' : '#01EFDD',
            'black' : '#000000'
        }
        self.title = "Hydre De Lerne"
        pygame.display.set_caption(self.title)
        
        #  au départ du jeu l'hydre n'existe pas
        #  elle est créée en fonction du niveau de difficulté donné par l'user
        self.hydre = None

        
    #TODO trouver une palette de couleur pour le jeu -> fait pr l'écran d'avant partie
    #TODO methode pour afficher l'Hydre sur le jeu 
    #TODO methode pour interagir avec l'hydre à l'aide de la souris -> fait pour l'écran d'avant partie
    def startMenu(self):
        """ Création d'un menu lorsqu'on entre dans le jeu pour choisir la difficulté 
            Lorsqu'un bouton est cliqué -> Renvoie le niveau de difficulté choisi
        """
        #arriere plan
        self.screen.fill(self.colors["blue"])

        #Affichage du texte en arriere plan en Jaune
        subtitle = self.titleFont.render("Hydre de Lerne", False,  self.colors["yellow"]) #création d'un objet surface avec notre texte
        subtitleSurf = subtitle.get_rect(center = (self.sizeX // 2, 140)) #on utilise getRect pr centrer plus facilement 
        
        self.screen.blit(subtitle,subtitleSurf)

        #Affichage du Titre en Violet
        title = self.titleFont.render("Hydre de Lerne", False,  self.colors["purple"])
        titleSurf = title.get_rect(center = (self.sizeX // 2, 130))
        self.screen.blit(title,titleSurf)

        #Affichage d'une phrase pour dire quoi faire à l'utilisateur
        textChooseLevel = self.textFontBold30.render("Choisissez la difficulté :", True, self.colors["purple"])
        textChooseLevelSurf = textChooseLevel.get_rect(center = (self.sizeX // 2, self.sizeY // 2 - 70))
        self.screen.blit(textChooseLevel, textChooseLevelSurf)

        #créations de 3 boutons - facile - moyen - difficile
        #Pour ce faire : objets surface
        # 1er btn -> niveau facile
        btnFacile = pygame.image.load(self.path + "\\hydreDeLerne\\images\\btnFacile.jpg").convert_alpha()
        btnFacileSurf = btnFacile.get_rect(center =(self.sizeX // 2, self.sizeY // 2))

        #On passe les coordonnées dans la classe pour pouvoir les réutiliser dans une autre méthodes
        self.coordxBtnFacile = (btnFacileSurf.topleft[0], btnFacileSurf.topright[0])
        self.coordyBtnFacile = (btnFacileSurf.topleft[1], btnFacileSurf.bottomleft[1])

        self.screen.blit(btnFacile, btnFacileSurf)

        #2eme btn -> niveau moyen
        btnMoyen = pygame.image.load(self.path + "\\hydreDeLerne\\images\\btnMoyen.jpg").convert_alpha()
        btnMoyenSurf = btnMoyen.get_rect(center = (self.sizeX // 2, (self.sizeY // 2) + 90))

        #On passe les coordonnées dans la classe pour pouvoir les réutiliser dans une autre méthodes
        self.coordxBtnMoyen = (btnMoyenSurf.topleft[0], btnMoyenSurf.topright[0])
        self.coordyBtnMoyen = (btnMoyenSurf.topleft[1], btnMoyenSurf.bottomleft[1])
        self.screen.blit(btnMoyen, btnMoyenSurf)


        #3eme btn -> niveau difficile
        btnDifficile = pygame.image.load(self.path + "\\hydreDeLerne\\images\\btnDifficile.jpg").convert_alpha()
        btnDifficileSurf = btnDifficile.get_rect(center = (self.sizeX // 2, (self.sizeY // 2) + 180))

        #On passe les coordonnées dans la classe pour pouvoir les réutiliser dans une autre méthode
        self.coordxBtnDifficile = (btnDifficileSurf.topleft[0], btnDifficileSurf.topright[0])
        self.coordyBtnDifficile = (btnDifficileSurf.topleft[1], btnDifficileSurf.bottomleft[1])
        self.screen.blit(btnDifficile, btnDifficileSurf)

        #On va mtn faire l'intéraction entre le joueur et le menu
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:#On écoute le clic
                        if event.button == 1:       #On cherche le clic droit
                            coord = event.pos       #On récupére ainsi la position du clic On a juste a regarder si la zone d'un bouton a été cliquée
                            if (self.coordxBtnFacile[0] <= coord[0] and coord[0] <= self.coordxBtnFacile[1]) and \
                               (self.coordyBtnFacile[0] <= coord[1] and coord[1] <= self.coordyBtnFacile[1]):
                                #Si le curseur se situe dans le bouton facile au clic on lance le jeu avec le niveau facile
                                print("facile")
                                self.outOfStart = True
                                return 'facile'
                            if (self.coordxBtnMoyen[0] <= coord[0] and coord[0] <= self.coordxBtnMoyen[1]) and \
                               (self.coordyBtnMoyen[0] <= coord[1] and coord[1] <= self.coordyBtnMoyen[1]):
                                #Si le curseur se situe dans le bouton moyen au clic on lance le jeu avec le niveau facile
                                print("moyen")
                                self.outOfStart = True
                                return 'moyen'
                            if (self.coordxBtnDifficile[0] <= coord[0] and coord[0] <= self.coordxBtnDifficile[1]) and \
                               (self.coordyBtnDifficile[0] <= coord[1] and coord[1] <= self.coordyBtnDifficile[1]):
                                #Si le curseur se situe dans le bouton difficile au clic on lance le jeu avec le niveau facile
                                print("difficile")
                                self.outOfStart = True
                                return 'difficile'
    def afficherHydre(self):
        """ Afficher l'Hydre avec laquelle on joue """
        #arriere plan
        self.screen.fill(self.colors['blue'])
        
        #Affichage en bas de l'écran, de différentes infos pour l'utilisateur
        footer = pygame.surface.Surface((self.sizeX, 50))
        footer.fill(self.colors['pink'])

        #affichage du nombre de coups
        nbreCoups = self.textFont30.render(f"Nombre de Coups : {self.hydre.nombreCoups}", True, self.colors['yellow'])

        #affichage du nombre de têtes restantes
        nbreTetes = self.textFont30.render(f"-  Nombre de Têtes restantes : {self.hydre.nombreTetes}", True, self.colors['yellow'])
        
        #bouton pour quitter le jeu
        btnQuit = pygame.surface.Surface((200, 40))
        btnQuit.fill(self.colors['yellow'])
        btnQuitCoordx = (self.sizeX - 250, self.sizeX - 50)
        btnQuitCoordy = (self.sizeY - 45, self.sizeY - 5)

        #tetxe du btn quitter
        textQuit = self.textFont30.render("Abandonner", True, self.colors['purple'])
        textQuitSurf = textQuit.get_rect(center = (btnQuit.get_rect().size[0] // 2, btnQuit.get_rect().size[1] // 2))


        footer.blit(nbreCoups, (0, 10))
        footer.blit(nbreTetes, (nbreCoups.get_rect().size[0] + 50, 8))
        btnQuit.blit(textQuit, textQuitSurf)
        footer.blit(btnQuit, (self.sizeX - 250, 5))
        self.screen.blit(footer, (0, self.sizeY - 50))
        
        #Affichage de l'hydre
        imageTete = pygame.image.load(self.path + "\\hydreDeLerne\\images\\TeteYellow.jpg").convert_alpha()
        imageTete = pygame.transform.scale(imageTete, (50,75))
        #Création d'un objet surface 'node'
        node = pygame.surface.Surface((50,50))
        node.fill(self.colors['yellow'])

        #On va ajouter une elt surface à chaque tête, cet elt est l'image teteYellow.jpg ou node(carré jaune de 50x50)
        index = 1
        countTete = 0
        pile = []
        pile.append(self.hydre)
        while len(pile) != 0:
            if pile[-1].estFeuille():
                pile[-1].setSurf(imageTete) #On attribue une surface à la tête
                index += 1
                countTete += 1
            else:
                pile[-1].setSurf(node)
            for enfant in pile.pop().getChildren():
                if not enfant.estVide():
                    pile.append(enfant)
            
        """
        #Affichage du corps
        corps = pygame.surface.Surface((50, 50))
        corps.fill(self.colors['yellow'])
        corpsSurf = corps.get_rect(center = (self.sizeX // 2, self.sizeY - 75))
        self.screen.blit(corps, corpsSurf)
"""
        # Affichage des têtes
        # 1ere étape partager l'écran pour allouer un espace égal à chque tête
        # Si il y a + de 20 tetes dans un étage, utiliser 2 étages
        
        #1ere etape
            #création d'un espace pour chaque tête
        listeAlloc = [[pygame.surface.Surface((self.sizeX // len(self.hydre.getEtage(j)), 81)) for i in range(len(self.hydre.getEtage(j)))] for j in range(self.hydre.hauteur()+1)]
        listeSurfaces = [[tete.getSurf() for tete in self.hydre.getEtage(j)] for j in range(self.hydre.hauteur() + 1)]
        
        
        #1ere etape , 2eme partie -> on lit chaque tete/node à son espace reservé
        
        for i in range(self.hydre.hauteur() + 1):
            for j in range(len(self.hydre.getEtage(i))):
                allocSize = listeAlloc[i][j].get_rect().size
                listeAlloc[i][j].blit(listeSurfaces[i][j], listeSurfaces[i][j].get_rect(center = (allocSize[0] // 2, allocSize[1] // 2)))
                self.screen.blit(listeAlloc[i][j], (j * allocSize[0], i * 81))
               
        #gestionnaire d'evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coord = event.pos
                    if  (btnQuitCoordx[0] <= coord[0] and coord[0] <= btnQuitCoordx[1]) and  \
                        (btnQuitCoordy[0] <= coord[1] and coord[1] <= btnQuitCoordy[1]):
                        #self.running  = False #Provisoire -> en attendant un écran de fin
                        self.gameEnd = True
                        return 'défaite'
                    
    def endMenu(self, result):
        if result == 'défaite' or result == 'victoire':
            if result == 'défaite':
                message = self.hydre.defaite()
                textBtn = 'Réessayer'
            else:
                textBtn = 'Rejouer'
                message = self.hydre.victoire()
            
            self.screen.fill(self.colors['blue'])

            #Affiche du msg de defaite/victoire
            textVictoireSub = self.titleFont.render(result, True, self.colors['yellow'])
            textVictoireSubSurf = textVictoireSub.get_rect(center = (self.sizeX // 2, self.sizeY - round(2 / 3 * self.sizeY) + 10))
            textVictoire = self.titleFont.render(result, True, self.colors['purple'])
            textVictoireSurf = textVictoire.get_rect(center = (self.sizeX // 2, self.sizeY - round(2 / 3 * self.sizeY)))
            self.screen.blit(textVictoireSub, textVictoireSubSurf)
            self.screen.blit(textVictoire, textVictoireSurf)

            message = self.textFontBold30.render(message, True, self.colors['yellow'])
            self.screen.blit(message, message.get_rect(center = (self.sizeX // 2, self.sizeY - 325)))
            #création de 2 boutons -> réessayer et quitter 
            #bouton réessayer
            btnRetry = pygame.surface.Surface((textVictoireSurf.size[0] // 2 - 50, 40))
            btnRetry.fill(self.colors['yellow'])
            btnRetrySurf = btnRetry.get_rect()
            btnRetryText = self.textFontBold30.render(textBtn, True, self.colors['purple'])
            textRetrySurf = btnRetryText.get_rect(center = (btnRetrySurf.size[0] // 2,btnRetrySurf.size[1] // 2 ))
            btnRetry.blit(btnRetryText, textRetrySurf)
            self.screen.blit(btnRetry, (textVictoireSurf.topleft[0], self.sizeY - 250))

            #coordonnées du btn réessayer
            btnRetryCoordx = (textVictoireSurf.left, textVictoireSurf.left + textVictoireSurf.size[0] // 2 - 50)
            btnRetryCoordy = (self.sizeY - 300, self.sizeY - 210)
            
            #bouton quitter
            btnQuit = pygame.surface.Surface((textVictoireSurf.size[0] // 2 - 50, 40))
            btnQuit.fill(self.colors['yellow'])
            btnQuitSurf = btnQuit.get_rect()
            btnQuitText  = self.textFontBold30.render("Quitter le jeu", True, self.colors['purple'])
            textQuitSurf = btnQuitText.get_rect(center = (btnQuitSurf.size[0] // 2, btnQuitSurf.size[1] // 2))
            btnQuit.blit(btnQuitText, textQuitSurf)
            self.screen.blit(btnQuit, (textVictoireSurf.topright[0] - textVictoireSurf.size[0] // 2 + 50, self.sizeY - 250))
            
            #coordonnées du btn quitter
            btnQuitCoordx = (textVictoireSurf.right - btnQuitSurf.size[0], textVictoireSurf)
            btnQuitCoordy = (self.sizeY - 300, self.sizeY - 210)

            #gestionnaire d'événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        coord = event.pos
                        if (btnRetryCoordx[0] <= coord[0] and coord[0] <= btnRetryCoordx[1]) and \
                           (btnRetryCoordy[0] <= coord[1] and coord[1] <= btnRetryCoordy[1]):
                            self.outOfStart = False
                            self.gameEnd = False
                            
                        if (btnQuitCoordx[0] <= coord[0] and coord[0] <= btnQuitCoordx[1]) and \
                           (btnQuitCoordy[0] <= coord[1] and coord[1] <= btnQuitCoordy[1]):
                            self.running = False
    def loop(self):
        while self.running:
            while not self.outOfStart and self.running:
                #On affiche d'abord le menu de démarrage
                startMenuReturnValue = self.startMenu()
                #Tant qu'on est pas sorti du menu ; on boucle sur le menu
                #Affiche le contenu à l'utilisateur

                #Si un bouton est cliqué, startMenu renvoie une valeur différente de None
                if startMenuReturnValue != None:
                     self.outOfStart = True

                pygame.display.update() #applique les modifs qu'on a fait à la page
                self.clock.tick(7) #regle le jeu à 10 fps

            self.hydre = createHydre(startMenuReturnValue)
            pygame.display.update()
            
            result = self.afficherHydre()
            print(result)
            while self.running and self.gameEnd:
                #Si l'utilisateur termine ou abandonne
                if result == "défaite" or result == "victoire":
                    self.endMenu(result)
                pygame.display.update()
                self.clock.tick(7)
            self.clock.tick(7) #regle le jeu à 10 fps

jeu = Game()
jeu.loop()

