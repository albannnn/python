from createHydre import createHydre
import random
import Hydre
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

        #attributs liés aux dimensions
        self.sizeX = 1280
        self.sizeY = 720
        self.screen = pygame.display.set_mode((self.sizeX, self.sizeY))

        #fonts
        self.titleFont = pygame.font.Font(self.path + "HydreDeLerne\\font\\Lazer84.ttf", 140)
        self.textFontBold30 = pygame.font.Font(self.path + "HydreDeLerne\\font\\DejaVuSansMono-Bold.ttf", 30)
        self.textFontBold15 = pygame.font.Font(self.path + "HydreDeLerne\\font\\DejaVuSansMono-Bold.ttf", 15)
        self.textFont30 = pygame.font.Font(self.path + "HydreDeLerne\\font\\DejavuSansMono.ttf", 30)
        self.textFont15 = pygame.font.Font(self.path + "HydreDeLerne\\font\\DejavuSansMono.ttf", 15)

        #fps 
        self.clock = pygame.time.Clock()

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
        self.icon = pygame.image.load(self.path + "\\HydreDelErne\\images\\TeteYellow.jpg").convert_alpha()
        pygame.display.set_icon(self.icon)
        
        #Infos reltive à l'Hydre
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
                                return 'moyen'
    def afficherHydre(self):
        """ Afficher l'Hydre avec laquelle on joue """
        #arriere plan
        self.screen.fill(self.colors['blue'])
        
        #Affichage en bas de l'écran, de différentes infos pour l'utilisateur
        footer = pygame.surface.Surface((self.sizeX, 50))
        footer.fill(self.colors['pink'])

        #affichage du nombre de coups
        nbreCoups = self.textFont30.render(f"Nombre de Coups : {self.hydre.nombreCoups}", True, self.colors['black'])

        #affichage du nombre de têtes restantes
        nbreTetes = self.textFont30.render(f"-  Nombre de Têtes restantes : {self.hydre.nombreTetes}", True, self.colors['black'])
        
        #bouton pour quitter le jeu
        btnQuit = pygame.surface.Surface((200, 40))
        btnQuit.fill(self.colors['yellow'])
        btnQuitCoordx = (self.sizeX - 250, self.sizeX - 50)
        btnQuitCoordy = (self.sizeY - 45, self.sizeY - 5)

        #tetxe du btn quitter
        textQuit = self.textFont30.render("Quitter", True, self.colors['black'])
        textQuitSurf = textQuit.get_rect(center = (btnQuit.get_rect().size[0] // 2, btnQuit.get_rect().size[1] // 2))


        footer.blit(nbreCoups, (0, 5))
        footer.blit(nbreTetes, (nbreCoups.get_rect().size[0] + 50, 5))
        btnQuit.blit(textQuit, textQuitSurf)
        footer.blit(btnQuit, (self.sizeX - 250, 5))
        self.screen.blit(footer, (0, self.sizeY - 50))
        
        #Affichage de l'hydre
        listeTetes = [pygame.image.load(self.path + "\\images\\TeteYellow.jpg").convert_alpha() for i in range(self.hydre.nombreTetes)]
        
        
        #gestionnaire d'evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coord = event.pos
                    if  (btnQuitCoordx[0] <= coord[0] and coord[0] <= btnQuitCoordx[1]) and  \
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
                self.clock.tick(60) #regle le jeu à 60 fps
            self.hydre = createHydre(startMenuReturnValue)
            pygame.display.update()
            self.afficherHydre()
            
        

jeu = Game()
jeu.loop()
