import customtkinter

#creation du fichier de configuration projet


#creation du dossier de sauvegarde projet

class App(customtkinter.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        #largeur de l'ecrant
        window_width = 1080 
        #hauteur de l'ecrant
        window_height = 720
        # recuperer la largeur et la hauteur de l'ecrant present
        screen_width = self.winfo_screenwidth() 
        screen_height = self.winfo_screenheight()
        
        #definir un position en x et y de la fenaitre: centrer la fenaitre
        x = (screen_width // 2) - (window_width // 2) 
        y = (screen_height // 2) - (window_height // 2)
        #nom du logiciel
        self.title("RegCadas")
        #def la taille de l'afficharge
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        #def une icone
        self.iconbitmap("regcadas/res/icone.ico")
        
        # configuration des grige a afficharge 4x4
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((1, 1, 1), weight=0)


if __name__ == "__main__":
    myapp = App()
    myapp.mainloop()