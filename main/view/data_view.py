
import customtkinter as ctk
import os
from PIL import Image, ImageTk

class DataView(ctk.CTk):
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
        self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure((1, 3), weight=1)
        # self.grid_rowconfigure((1, 1, 1), weight=1)
        
        #chargement des image
        acualise_icon = Image.open("res/image/actualiser.png")
        imprimente_icon = Image.open("res/image/imprimente_noir.png")
        suprime_icon = Image.open("res/image/suprimer.png")
        
        
        #configuration d l'image pour le btn parametre
        self.actualiser = ctk.CTkImage(light_image=acualise_icon, dark_image=acualise_icon, size=(20, 20))
        self.imprimer = ctk.CTkImage(light_image=imprimente_icon, dark_image=imprimente_icon, size=(20, 20))
        self.suprimer = ctk.CTkImage(light_image=suprime_icon, dark_image=suprime_icon, size=(20, 20))

        #frame de visualisation
        self.view_frame = ctk.CTkFrame(master=self,)
        self.view_frame.grid_columnconfigure(0, weight=1)
        self.view_frame.grid(row=0, column=0, sticky="ew")
        ###################################################################################################
        #frame pour la bare des outils
        self.tools_frame = ctk.CTkFrame(master=self.view_frame, height=100,corner_radius=10, border_color=None)
        self.tools_frame.grid_columnconfigure((1,3,), weight=1)
        self.tools_frame.grid(row=0, column=0, sticky="ew",padx=x)
        
        # #definir une bare de rechercher positioner a la droite de la bare d'outils
        self.search = ctk.CTkEntry(master=self.tools_frame, placeholder_text="Recherche").grid(row=0, column=2, padx=10,sticky="w")
        
        #definir les option de filtrage par arrd
        self.arrd_option = ctk.CTkOptionMenu(
            master=self.tools_frame,
            bg_color="transparent",
            fg_color=None, 
            values=["MFOU", "ESSE", "AFANLOUM", "NKOLAFAMBA", "SOA", "OLANGUINA", "AWAE", "EDZENDUOAN"],
            ).grid(row=0, column=1, pady=5, padx=10,sticky="w")
        
        #definir les option de filtrage par saisire
        self.typing_option = ctk.CTkOptionMenu(
            master=self.tools_frame,
            values=[
                "Immatriculation directe",
                "Morcelement",
                "Concession définitive",
                "Dossier technique de levé"]
            ).grid(row=0, column=0, pady=5,padx=10,sticky="w")
        
        #define bonton pour imprimer
        self.reload_btn = ctk.CTkButton(
            master=self.tools_frame,
            text="", image=self.imprimer, 
            width=30, 
            height=30, 
            corner_radius=3, 
            bg_color="transparent", 
            fg_color="transparent",
            ).grid(row=0, column=3, pady=5,padx=10,sticky="w")
        
        #define bonton pour actualiser l'afficharge
        self.reload_btn = ctk.CTkButton(
            master=self.tools_frame,
            text="", image=self.actualiser, 
            width=30, 
            height=30, 
            corner_radius=3, 
            bg_color="transparent", 
            fg_color="transparent",
            ).grid(row=0, column=4, pady=5,padx=10,sticky="w")
        
        #define bonton pour actualiser l'afficharge
        self.reload_btn = ctk.CTkButton(
            master=self.tools_frame,
            text="", image=self.suprimer, 
            width=30, 
            height=30, 
            corner_radius=3, 
            bg_color="transparent", 
            fg_color="transparent",
            ).grid(row=0, column=5, pady=5,padx=10,sticky="w")
        ###################################################################################################
        
        #frame de liste visuel
        self.list_view = ctk.CTkFrame(master=self.view_frame,)
        self.list_view.grid(row=1, column=0, sticky="we",)
        self.list_view.grid_columnconfigure(0, weight=1)
        
        tabs_names = [
            "Numero","Requerent","Nature","Geometre","Lieu","Arrondissement","Superficie","Paquet N"
        ]
        
        # # #definir une bare d'oblet des different reference
        self.ref_tabs = ctk.CTkFrame(master=self.list_view, height=50,)
        self.ref_tabs.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1)
        self.ref_tabs.grid(row=0, column=0, sticky="we")
        # #boucle pour afficher tout les onglets
        for i in range(len(tabs_names)):
            tabs_list = ctk.CTkLabel(master=self.ref_tabs, text=tabs_names[i])
            tabs_list.grid(row=0, column=i, sticky="we", padx=5)
        
        #definir un frame scrollable ou les element vont etre afficher
        self.scrallable_list = ctk.CTkScrollableFrame(master=self.list_view, fg_color="blue")
        self.scrallable_list.grid(row=1, column=0, sticky="wes")
        
        
        

if __name__ == "__main__":
    app = DataView()
    app.mainloop()