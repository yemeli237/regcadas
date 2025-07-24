import customtkinter
import os
from PIL import Image, ImageTk
from view.config import *
from Ajouter import ajoute_window
from visual import visual_window

#creation du fichier de configuration projet
doc = os.path.join(os.path.expanduser("~"), "Documents")
dossier = "Regcadas"
save_dir = os.path.join(doc, dossier)
if os.path.exists(save_dir) :
    print("Creation du dossier de sauvegarde dans la bibliotheque Document")
else:
    os.mkdir(save_dir)
    print("le dossier de sauvegarde existe deja")
    
config = {}
#creation du fichier de configuration projet
docs = os.path.join(os.path.expanduser("~"), "Documents/BT")
dossiers = "Config"
config_dir = os.path.join(docs, dossiers)
# if os.path.exists(config_dir):
#     pass
# else:
#     os.makedirs(config_dir)

#charger le fichier des configuration
#si le ficchier existe, on le charge et on applique les modifications
if os.path.exists(config_dir):
    if os.path.exists(f"{config_dir}/config.json"):
        with open(f"{config_dir}/config.json", "r") as confg:
            config = json.load(confg)
        if config["theme"] != "":
            customtkinter.set_appearance_mode(f"{config["theme"]}")
            customtkinter.set_widget_scaling(config["scale"])


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
        # self.iconbitmap("regcadas/res/icone.ico")
        self.iconbitmap("res/icone.ico")
        # self.iconbitmap("icone.ico")
        
        # configuration des grige a afficharge 4x4
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 2), weight=0)
        self.grid_rowconfigure((1, 1, 1), weight=1)
        
        # creer la barre laterale gauche grang fromat
        self.sidebar_frame = customtkinter.CTkFrame(self, width=400, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        #creer lle frame de l'interface de visualisation
        # self.main_screen = ajoute_window(parent=self).grid(row=0, column=1)
        
        # creer la barre laterale gauche minimaliser
        self.sidebar_frame_min = customtkinter.CTkFrame(self, width=100, corner_radius=0)
        # self.sidebar_frame_min.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame_min.grid_rowconfigure(4, weight=1)
        # self.sidebar_frame_min.forget()
        
        
        
        #chargement des icone avec PIL
        # param_img = Image.open("../res/image/param.png")
        # data_img = Image.open("../res/image/explore_data.png")
        # reduice_img = Image.open("../res/image/reduice.png")
        # add_data_img = Image.open("../res/image/add_data.png")
        
        ####################
        param_img = Image.open("res/image/param.png")
        data_img = Image.open("res/image/explore_data.png")
        reduice_img = Image.open("res/image/reduice.png")
        add_data_img = Image.open("res/image/add_data.png")
        
        
        #configuration d l'image pour le btn parametre
        self.img = customtkinter.CTkImage(light_image=param_img, dark_image=param_img, size=(30, 30))
        #conficurationde l'image pour le btn des donne
        self.explore_data_img = customtkinter.CTkImage(light_image=data_img, dark_image=data_img, size=(30, 30))
        #conficurationde l'image pour le btn de reduction d'interface
        self.reduice_frame_img = customtkinter.CTkImage(light_image=reduice_img, dark_image=reduice_img, size=(10, 10))
        #conficurationde l'image pour le btn d'ajout des donnees
        self.add_data_frame_img = customtkinter.CTkImage(light_image=add_data_img, dark_image=add_data_img, size=(30, 30))
        
        self.main_screen = visual_window(parent=self)
        self.entry_screen = ajoute_window(parent=self)
        self.main_screen.grid(row=0, column=1)
        
        #bouton pour gerer les donnes
        self.dashbor = customtkinter.CTkButton(
            master=self.sidebar_frame,
            text="Gestion", image=self.explore_data_img, 
            width=30, 
            height=30, 
            corner_radius=3, 
            bg_color="transparent", 
            fg_color="transparent",
            text_color="#007acc",
            # command=self.agranddir
            command=self.ouvrir_gestion  # appel de la fonction qui ouvre la fenêtre de gestion
        ).grid(row=1, column=0, padx=10, pady = 10)
        
        #bouton pour ajouter les nouvelle donne
        self.add_data = customtkinter.CTkButton(
            master=self.sidebar_frame,
            text="Ajouter", image=self.add_data_frame_img, 
            width=30, 
            height=30, 
            corner_radius=3, 
            bg_color="transparent", 
            fg_color="transparent",
            text_color="#007acc",
            #command=self.agranddir
            command=self.ouvrir_ajout  # appel de la fonction qui ouvre la fenêtre Ajouter
        ).grid(row=2, column=0, padx=10, pady = 10)
        #btn pour ouvrir le menu
        self.param_btn = customtkinter.CTkButton(
            master=self.sidebar_frame,  
            text="Parametre", image=self.img, 
            width=30, 
            height=30, 
            corner_radius=3, 
            bg_color="transparent", 
            fg_color="transparent",
            text_color="#007acc",
            command= self.config
            )
        self.param_btn.grid(row=8, column=0, padx=10, pady=10)
        
        #creer un bouton pour reduire la fenetre lateral gauche
        self.close_btn = customtkinter.CTkButton(
            master=self.sidebar_frame,
            text="", image=self.reduice_frame_img, 
            width=30, 
            height=30, 
            corner_radius=3, 
            bg_color="transparent", 
            fg_color="transparent",
            command=self.reduice
        ).grid(row=8, column=1)
        
        #afficharge lateralle reduite
        #bouton pour gerer les donnes
        self.dashbor = customtkinter.CTkButton(
            master=self.sidebar_frame,
            text="Gestion", image=self.explore_data_img, 
            width=30, 
            height=30, 
            corner_radius=3, 
            bg_color="transparent", 
            fg_color="transparent",
            text_color="#007acc",
            # command=self.agranddir,
            command=self.ouvrir_gestion
        ).grid(row=1, column=0, padx=10, pady = 10)
        
        ########################################bouton pour ajouter les nouvelle donne
        #bouton pour gerer les donnees
        self.add_data = customtkinter.CTkButton(
            master=self.sidebar_frame_min,
            text="", image=self.explore_data_img, 
            width=30, 
            height=30, 
            corner_radius=3, 
            bg_color="transparent", 
            fg_color="transparent",
            text_color="#007acc",
            command=self.agranddir
        ).grid(row=1, column=0, padx=10, pady = 10)
        ##bouton pour ajouter les nouvelle donne
        self.add_data = customtkinter.CTkButton(
            master=self.sidebar_frame_min,
            text="", image=self.add_data_frame_img, 
            width=30, 
            height=30, 
            corner_radius=3, 
            bg_color="transparent", 
            fg_color="transparent",
            text_color="#007acc",
            command=self.agranddir,
            #command = self.ouvrir_ajout  # appel de la fonction qui ouvre la fenêtre Ajouter
        ).grid(row=2, column=0, padx=10, pady = 10)
        #btn pour ouvrir le menu
        self.param_btn = customtkinter.CTkButton(
            master=self.sidebar_frame_min,  
            text="", image=self.img, 
            width=30, 
            height=30, 
            corner_radius=3, 
            bg_color="transparent", 
            fg_color="transparent",
            text_color="#007acc",
            command= self.config
            )
        self.param_btn.grid(row=8, column=0, padx=10, pady=10)
        

        
        
        
        
    ############# section des fonctions
    #fonction pour ouvrir l'interface des parametre
    def config(self):
        ouvrir_parametre(self)
        
    def agranddir(self):
        largeur_actuel = self.sidebar_frame.cget("width")
        nouvelle_largeur = largeur_actuel + 200
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame_min.grid_forget()
    
    #fonction pour reduire la fenaitre laterale gauche
    def reduice(self):
        print("reduite")
        largeur_actuel = self.sidebar_frame.cget("width")
        nouvelle_largeur = largeur_actuel - 100
        self.sidebar_frame.grid_forget()
        self.sidebar_frame_min.grid(row=0, column=0, rowspan=4, sticky="nsew")

    def ouvrir_ajout(self):
        self.main_screen.grid_forget()
        self.entry_screen.grid(row=0, column=1)
        
    def ouvrir_gestion(self):
        self.entry_screen.grid_forget()
        self.main_screen.grid(row=0, column=1)


if __name__ == "__main__":
    myapp = App()
    myapp.mainloop()