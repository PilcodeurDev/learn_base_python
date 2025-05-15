# le document permet de rendre persistant les données, de les sauvegarger sur l'ordinateur
# Pour créer un nouveau document on utilise la fonction de python appeler : open() qui demande deux arguments:
# 1) "nom du fichier.nom de l'extention"
# 2) mode d'ouverture de fichier :
# "w", "w+" : écrit sur le fichier (écrase le contenu)
# "a" : ajoute sur le fichier ( sans écraser le contenu)
# "r" : lire le fichier
# exemple : open("students.txt", "w+")
# pour travaller dans ce fichier il faut le stocker sous la forme d'une variable.
# exemple : file = open("students.txt", "w+")

# file = open("students.txt", "w+")
# file.write("Paul\n")
# file.write("Jean\n")
# file.write("Martin\n")

# mots clefs 1) "with" est plus approprié pour créer et modifier le contenu de fichier : permet de récupérer le contexte de ce qu'on as après ce mot clef. 2) "as" nous permet de nommer le fichier et de travailler avec ce nom.

students_list = ["Rodrigue", "Amélie", "Laurent", "Gwendoline", "Manon", "Meggane"]

with open("students.txt", "w+") as file:
    for student in students_list:
        file.write(student + "\n")

    #obligatoire a chaque fin de fichier
    file.close()
