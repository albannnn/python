import tkinter as tk
import Hydre

    
        
class App(tk.Tk):
    def __init__(self, fullscreen = False):
        tk.Tk.__init__(self)
        #On donne un titre et on mets une nouvelle image en favicon
        self.title("Hydre De Lerne")
        self.iconbitmap(r"d:\dev\hydreDeLerne\favicon.ico")
        if fullscreen:
            self.attributes('-fullscreen', True)
        
        else:
            #Définitions des coordonnées et placement de la page sur l'écran
            self.sizeX = 800
            self.sizeY = 600
            self.screenSize = (self.winfo_screenwidth(), self.winfo_screenheight())
            self.coordX = (self.screenSize[0] // 2) - self.sizeX // 2
            self.coordY = (self.screenSize[1] // 2) - self.sizeY // 2

            #On centre la fenetre au milieu de l'écran
            self.geometry(f"{self.sizeX}x{self.sizeY}+{self.coordX}+{self.coordY}")
        self.bind("<F11>",
                  lambda event: self.attributes("-fullscreen",
                            not self.attributes("-fullscreen")))
        self.bind("<Escape>",
                  lambda event: self.attributes("-fullscreen", False))
        #TODO 1°: Trouver un moyen de reprèsenter chaque partie de l'hydre
        #TODO 2°: Trouver un moyen de reprèsenter l'hydre toute seule
        #TODO 3°: Faire l'interaction entre utilisateur et la machine
    def coordMilieuElt(self, xElt = 0, yElt = 0):
        milieuX = self.sizeX // 2 - xElt
        milieuY = self.sizeY // 2 - yElt
        return (milieuX, milieuY)
    
    def dessineCorps(self):
        canva = tk.Canvas(self, width=250, height=250)
        
        
        canva.pack(side="bottom")
if __name__ == "__main__":
    app = App(fullscreen = True)
    app.dessineCorps()
    app.mainloop()


    
        

