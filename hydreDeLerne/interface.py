import tkinter as tk
import tkinter.font as tkFont

import random
import Hydre


    
        
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #On donne un titre et on mets une nouvelle image en favicon
        self.title("Hydre De Lerne")
        self.iconbitmap(r"d:\dev\hydreDeLerne\favicon.ico")
        self.configure(bg="#5878B0")
        # Définitions des coordonnées
        self.screenSize = (self.winfo_screenwidth(),
                           self.winfo_screenheight())
        self.sizeX = 900
        self.sizeY = 650
        self.coordX = (self.screenSize[0] // 2) - self.sizeX // 2
        self.coordY = (self.screenSize[1] // 2) - self.sizeY // 2
        #place la fenetre au milieu de l'écran
        self.geometry(f"{self.sizeX}x{self.sizeY}+{self.coordX}+{self.coordY}")
        #Bind les commandes pour faire aller en plein écran et revenir
        self.bind("<F11>",
                  lambda event: self.attributes("-fullscreen",
                            not self.attributes("-fullscreen")))
        self.bind("<Escape>",
                  lambda event: self.attributes("-fullscreen", False))
        #TODO 1°: Faire l'écran d'accueil
        #TODO 2°: Trouver un moyen de représenter chaque partie de l'hydre
        #TODO 3°: Trouver un moyen de reprèsenter l'hydre toute seule
        #TODO 4°: Faire l'interaction entre utilisateur et la machine

    def welcomeScreen(self):
        """ Affichage de l'écran d'accueil où on pourra choisir la difficulté """
        conteneurTitre = tk.Frame(self, )
        
        titre = tk.Label(conteneurTitre, image =  )
        question = tk.Label(
            self, text="Choisissez la difficulté :", bg="#5878B0")
        conteneurTitre.pack()
        titre.pack()
        question.pack()

    def dessineCorps(self):
        canva = tk.Canvas(self, width = 250, height=250, bg='ivory')
        #Création des pattes
        
        #Création du corps en lui même
        canva.create_oval(62, 120, 188, 220, fill="#F6D342",
                          outline="black", width=3, activefill="#C58F0F")
        
        canva.pack(side="bottom")



if __name__ == "__main__":
    app = App()
    app.welcomeScreen()
    app.mainloop()


    
        

