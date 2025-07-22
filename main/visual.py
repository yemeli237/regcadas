
import os
from tkinter import Image, Tk, filedialog, messagebox
import customtkinter
from tkcalendar import DateEntry
from PIL import Image, ImageTk, ImageOps
import tkinter as TK

class visual_window(customtkinter.CTkFrame):#definir une classe qui vas represnter l'inteface d'entrer des donnes
    def __init__(self, parent, *ars, **kwargs):
        super().__init__(parent, *ars, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure((1, 3), weight=1)
        self.grid_rowconfigure((1, 1, 1), weight=1)
        
        #afficher le titre de l'interface actuelle
        title_label = customtkinter.CTkLabel(
            self,
            text="Archives du cadastre:",
            font=("Arial", 22, "bold"),
            # text_color="white"
        )
        title_label.pack(pady=20)