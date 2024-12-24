import tkinter as tk
from tkinter import messagebox


def automate_task():
    messagebox.showinfo("Automatisation", "Tâche exécutée avec succès !")


# Créer la fenêtre principale
root = tk.Tk()
root.title("Application d'Automatisation")

# Ajouter un bouton pour lancer une tâche
button = tk.Button(root, text="Lancer la tâche", command=automate_task)
button.pack(pady = 20)

# Lancer l'application
root.mainloop()
