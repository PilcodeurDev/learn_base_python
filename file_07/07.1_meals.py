# Créer un fichier .txt avec une listes de plusieurs nom de repas.
# Cherche un repas au hasard
import os
import random

# Vérifie si le nom de fichier existe
if os.path.exists("meals.txt"):
    with open("meals.txt", "r+") as file:
        # Lire toute les lignes du document
        #print(file.readlines())
        meals_list = file.readlines()
        meal_choice = random.choice(meals_list)
        print("Aujourd'hui, je vous propose de manger :", meal_choice)
    file.close

else:
    print("Le document n'existe pas.")
