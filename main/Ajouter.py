import os
from tkinter import filedialog, messagebox
import customtkinter
from tkcalendar import DateEntry


class AjoutWindow(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ajouter une archive")
        self.geometry("1200x1000")
        self.lift()
        self.focus_force()
        self.grab_set()

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

        title_label = customtkinter.CTkLabel(
            self,
            text="Enregistrez vos archives ici :",
            font=("Arial", 22, "bold"),
            text_color="white"
        )
        title_label.pack(pady=20)

        self.create_form(self)

    def create_form(self, parent):
        form_frame = customtkinter.CTkFrame(parent, corner_radius=10)
        form_frame.pack(pady=20, padx=20, fill="both", expand=True)

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

        # Image
        def choisir_image():
            chemin = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp")])
            if chemin:
                self.image_path = chemin
                self.image_label.configure(text=os.path.basename(chemin))

        image_row = (len(field_labels) + 2) // 3
        self.image_label = customtkinter.CTkLabel(
            form_frame,
            text="Aucune image sélectionnée",
            text_color="#007acc"
        )
        image_button = customtkinter.CTkButton(
            form_frame,
            text="Joindre une image",
            command=choisir_image,
            fg_color="#007acc",
            hover_color="#005b99",
            text_color="white"
        )
        self.image_label.grid(row=image_row, column=0, columnspan=2, padx=10, pady=10, sticky="e")
        image_button.grid(row=image_row, column=2, columnspan=2, padx=10, pady=10, sticky="w")

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
