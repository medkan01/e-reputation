import os

# Chemin vers le dossier contenant vos scripts
folder_path = r"D:/Lorraine/Scripts"

# Liste des fichiers .py dans le dossier, en excluant main_script.py
files = [f for f in os.listdir(folder_path) if f.endswith(".py") and f != "planification.py"]

# Exécution de chaque fichier .py trouvé
for file in files:
    full_path = os.path.join(folder_path, file)
    os.system(f"python {full_path}")
