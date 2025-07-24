import os
from tkinter import Image, Tk, filedialog, messagebox
import customtkinter
from tkcalendar import DateEntry
from PIL import Image, ImageTk, ImageOps
import tkinter as TK





class ajoute_window(customtkinter.CTkFrame):#definir une classe qui vas represnter l'inteface d'entrer des donnes
    def __init__(self, parent, *ars, **kwargs):
        super().__init__(parent, *ars, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure((1, 3), weight=1)
        self.grid_rowconfigure((1, 1, 1), weight=1)
        #definir les valeur par defaut
        self.default_values = {
            "Region": "CENTRE",
            "Departement": "MEFOU ET AFAMBA",
            "Arrondissement": ["MFOU", "ESSE", "AFANLOUM", "NKOLAFAMBA", "SOA", "OLANGUINA", "AWAE", "EDZENDUOAN"],
            "Nature du Travail": [
                "Immatriculation directe",
                "Morcelement",
                "Concession définitive",
                "Dossier technique de levé"
            ]
        }
        #afficher le titre de l'interface actuelle
        title_label = customtkinter.CTkLabel(
            self,
            text="Enregistrez vos archives ici :",
            font=("Arial", 22, "bold"),
            # text_color="white"
        )
        title_label.pack(pady=20)
        self.create_form(self)
    #formulaire pour recupere les donnees
    def create_form(self, parent):
        form_frame = customtkinter.CTkFrame(parent, corner_radius=10)
        form_frame.pack(pady=5, padx=5, fill="both", expand=True)
        #les different champs a remplir
        field_labels = [
            "Region", "Departement", "Arrondissement", "Quartier", "DTN No",
            "Lieu-dit", "Nature du Travail", "Requerant", "Superficie",
            "HA", "A ", "CA", "Levé Par",
            "Le", "TF No ", "Calculé Par", "Le",
            "CCP", "MCP"
        ]

        self.entries = {}
        self.image_path = None

        for i, label_text in enumerate(field_labels):
            label = customtkinter.CTkLabel(
                form_frame,
                text=label_text,
                text_color="#007acc",
                font=("Arial", 12, "bold")
            )

            row = i // 3
            col = (i % 3) * 2
            label.grid(row=row, column=col, padx=(10, 5), pady=8, sticky="e")

            if label_text == "Region":
                entry = customtkinter.CTkEntry(form_frame, width=300)
                entry.insert(0, self.default_values["Region"])

            elif label_text == "Departement":
                entry = customtkinter.CTkEntry(form_frame, width=300)
                entry.insert(0, self.default_values["Departement"])

            elif label_text == "Arrondissement":
                entry = customtkinter.CTkOptionMenu(form_frame, values=self.default_values["Arrondissement"])
                entry.set(self.default_values["Arrondissement"][0])

            elif label_text == "Nature du Travail":
                entry = customtkinter.CTkOptionMenu(form_frame, values=self.default_values["Nature du Travail"], width=300)
                entry.set(self.default_values["Nature du Travail"][0])

            elif label_text.strip() == "Le":
                entry = DateEntry(form_frame, width=23, background='darkblue', foreground='white', borderwidth=2)

            else:
                placeholder = f"Entrer {label_text.lower()}"
                entry = customtkinter.CTkEntry(
                    form_frame,
                    width=300,
                    height=40,
                    corner_radius=10,
                    fg_color="#f7faff",
                    text_color="#000000",
                    border_color="#007acc",
                    border_width=1,
                    placeholder_text=placeholder
                )

            entry.grid(row=row, column=col + 1, padx=(0, 20), pady=8, sticky="w")
            self.entries[label_text] = entry
###################################################################
        # charger l'image et montre une apercus
        def choisir_image():
            try:
                root = Tk()#initialier un root pour le filedialog
                root.withdraw()
                root.title("Importer une image")#definir un titre
                path = filedialog.askopenfile(filetypes=[("Image",  ".png .jpeg .svg .jpg")], title="Ajouter une Image", parent=self)
                chemin = path.name#recuperer le chemin d'acces a l'image
                self.image_path = path.name
                img_path = Image.open(f"{chemin}")#ouvrir l'image pour avoir un epercus
                img_path = ImageOps.exif_transpose(img_path)#placer a la bonne orientation
                img = customtkinter.CTkImage(light_image=img_path, dark_image=img_path, size=(200, 275))
                apercu_img = customtkinter.CTkLabel(master=form_frame, text="Apercu", image=img)
                apercu_img.grid(row=8, column=5)
                
                
                
            except Exception as e:
                print(e)
            # chemin = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp")], title="Ajouter une image")
            if chemin:
                self.image_path = chemin
                self.image_label.configure(text=os.path.basename(chemin))

        image_row = (len(field_labels) + 2) // 3
        self.image_label = customtkinter.CTkLabel(
            form_frame,
            text="Aucune image sélectionnée",
            text_color="#007acc",
        )
        
        
        
        image_button = customtkinter.CTkButton(
            form_frame,
            text="Joindre une image",
            command=choisir_image,
            fg_color="#007acc",
            hover_color="#005b99",
            text_color="white"
        )
        
        image_button.grid(row=8, column=1, columnspan=2, padx=10, pady=10, sticky="w")
        
##########################################################
        # Enregistrement
        def enregistrer_donnees():
            valeurs = {}
            for label, entry in self.entries.items():
                val = entry.get().strip() if hasattr(entry, "get") else ""
                if not val:
                    messagebox.showerror("Erreur", f"Veuillez remplir tous les champs (champ vide : {label})")
                    return
                valeurs[label] = val

            if not self.image_path:
                messagebox.showerror("Erreur", "Veuillez joindre une image.")
                return

            nature = valeurs["Nature du Travail"].lower()

            if "immatriculation" in nature:
                nom_fichier = "immatriculation.txt"
            elif "morcelement" in nature:
                nom_fichier = "morcelement.txt"
            elif "concession" in nature:
                nom_fichier = "concession.txt"
            elif "levé" in nature:
                nom_fichier = "dossier.txt"
            else:
                messagebox.showerror("Erreur", "Type de travail inconnu.")
                return

            try:
                os.makedirs("regcadas", exist_ok=True)
                chemin_fichier = os.path.join("regcadas", nom_fichier)

                with open(chemin_fichier, "a", encoding="utf-8") as f:
                    ligne = " | ".join([f"{key}: {valeurs[key]}" for key in valeurs])
                    ligne += f" | Image: {self.image_path}\n"
                    f.write(ligne)

                messagebox.showinfo("Succès", f"Données enregistrées dans {nom_fichier}")

                # Réinitialiser tout le formulaire (sauf valeurs par défaut)
                for label, entry in self.entries.items():
                    if label in self.default_values:
                        if label == "Nature du Travail":
                            entry.set(self.default_values[label][0])
                        elif label == "Arrondissement":
                            entry.set(self.default_values[label][0])
                        else:
                            entry.delete(0, "end")
                            entry.insert(0, self.default_values[label])
                    else:
                        entry.delete(0, "end")

                self.image_path = None
                self.image_label.configure(text="Aucune image sélectionnée")

            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l’enregistrement : {e}")

        enregistrer_btn = customtkinter.CTkButton(
            form_frame,
            text="Enregistrer",
            corner_radius=10,
            height=45,
            fg_color="#0059b3",
            hover_color="#004080",
            text_color="white",
            font=("Arial", 14, "bold"),
            command=enregistrer_donnees
        )
        enregistrer_btn.grid(row=image_row + 1, column=0, columnspan=6, pady=25)

