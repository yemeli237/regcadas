import customtkinter
import json
import os
from tkinter import *
from tkinter import filedialog
import tkinter as TK
from PIL import Image, ImageTk
from tkinter import Tk, filedialog

#creation du fichier de sauvegarde projet
doc = os.path.join(os.path.expanduser("~"), "Documents/Regcadas")
dossier = "Config"
project_dir = os.path.join(doc, dossier)
if os.path.exists(project_dir):
    pass
else:
    os.makedirs(project_dir)
placement = project_dir

#verifier si le fichier de sauvegarde du theme est present
if os.path.exists(f"{placement}/theme.json"):
    pass
else:
    try:
        with open(f"{placement}/theme.json", "w") as f:
            json.dump({"theme":""}, f)
    except Exception as e:
        print(e)
#verifier si le fichier de sauvegarde du l'echelle est present     
if os.path.exists(f"{placement}/scale.json"):
    pass
else:
    try:
        with open(f"{placement}/scale.json", "w") as f:
            json.dump({"scale":""}, f)
    except Exception as e:
        print(e)
        
def ouvrir_parametre(principal):#classe des parametres
    self = customtkinter.CTkToplevel(principal)
    self.title("Parametre")
    self.geometry("1080x620+100+100")
    self.attributes('-topmost', True)
    self.resizable(False, False)
    self.focus_force()
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure((1, 1), weight=0)
    self.grid_rowconfigure((1, 1, 1), weight=1)
    
    
    logo_label = customtkinter.CTkLabel(#titre de la fenaitre
        self, text="Parametre", 
        font=customtkinter.CTkFont(size=30, weight="bold"),
        text_color="#DC3F3F"
        )
    logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
    param_frame = customtkinter.CTkFrame(self, width=1000)#frame pour la configuration du theme
    param_frame.grid(row=1, column=0 , sticky="ns")
    #composant pour le parametre de theme
    valeur_theme = ["System", "Dark", "Light"]
        
    theme_frame = customtkinter.CTkFrame(master=param_frame, width=500)
    theme_frame.grid(row=1, column=0 , sticky="nsew", pady=10, padx=5,)
    theme_lable = customtkinter.CTkLabel(master=theme_frame, text="Theme")
    theme_lable.grid(row=0, column=3, sticky="nsew", padx=(100, 0), pady=(5, 10))
    echele_theme = customtkinter.CTkSegmentedButton(
            master=theme_frame, 
            values=valeur_theme, 
            command=lambda new_appearance_mode : apparence(new_appearance_mode),#fontion pour changer de them
            width=1000
            )
    echele_theme.grid(row=1, column=3, sticky="nsew", padx=(100, 0))
    
    #parametre pour le composant echelle
    valeur_echele = ["80%", "90%", "100%", "105%","110%","115%","120%","125%"]
        
    echele_frame = customtkinter.CTkFrame(master=param_frame, width=500)#frame pour changer d'echelle
    echele_frame.grid(row=2, column=0 , sticky="nsew", pady=10, padx=5,)
    echele_lable = customtkinter.CTkLabel(master=echele_frame, text="Echelle")
    echele_lable.grid(row=0, column=0, sticky="nsew") 
    echele_segment = customtkinter.CTkSegmentedButton(
            master=echele_frame,
            values=valeur_echele,
            command=lambda new_scaling :echelle(new_scaling)
            )
    echele_segment.grid(row=1, column=0, sticky="nsew", padx=(0, 0), pady=(5, 10))
    
    
            
    save_btn = customtkinter.CTkButton(master=self, text="Sauvegarder", command=saves)
    save_btn.grid(row=4, column=0, pady=5)
    #??????????????????????
    
    ############# section des fonctions
    

    
    def echelle( new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        with open(f"{placement}/scale.json", "w") as file:
            json.dump({"scale":new_scaling_float}, file)
        
    def apparence( new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
        with open(f"{placement}/theme.json", "w") as file:
            json.dump({"theme":new_appearance_mode}, file)
            
        #focntion pour sauvegarder les parametres           
def saves():
    #charger le fichier du theme        
    if os.path.exists(f"{placement}/theme.json"):
        with open(f"{placement}/theme.json", "r") as f:
            theme = json.load(f)
    #charger le fichier de l'echelle        
    if os.path.exists(f"{placement}/scale.json"):
        with open(f"{placement}/scale.json", "r") as f:
            scale = json.load(f)
    #organiser lesfichiers charge        
    config = {
            "scale": scale["scale"] or 1.0,
            "theme": theme["theme"] or "System",
        } 
    #sauvegarder la configuration
    with open(f"{placement}/config.json", "w") as confg:
        json.dump(config, confg, indent=4) 
        print("Sauvegarder avec succes") 
