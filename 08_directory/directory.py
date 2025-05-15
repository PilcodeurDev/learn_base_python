import json
# un directory (dictionaire) est une liste d'élements caractérisés par une clef et une valeur pour chaque element.

eleves = {
    "Paul": 12,
    "Marine": 15,
    "Thierry": 8,
}

# je demande la valeur de l'élement avec la clef "Paul"
print(eleves["Paul"])

# Chercher une clef dans ce directory "eleves", si elle existe, sinon affiche une valeur par defaut "Prenom".
# La clef existe :
print(eleves.get("Paul", "Prenom"))
# La clef n'existe pas :
print(eleves.get("Léa", "Prenom"))

# moyenne de la classe
total = sum(eleves.values()) / len(eleves)
print(total)
#moyenne arrondi
print(round(total))

# boucle qui affiche que les clefs :
for eleve in eleves:
    print(eleve)

# boucle qui affiche que les valeurs :
for eleve in eleves.values():
    print(eleve)

# boucle qui affiche l'élement entier avec ('clef', 'valeurs') :
for eleve in eleves.items():
    print(eleve)

# boucle qui affiche chaque information dans l'élément (la clef et la valeur) :
for prenom, moyenne in eleves.items():
    print(prenom, moyenne)
    # utilisation du f format : permet d'écrire du texte avec des variables en accolade
    print(f"La moyenne de {prenom} est de {moyenne}/20.")

# La valeur peut etre un string, int, un array, un direcotry :
classe = {
    "Théo" : {
        "note" : 12,
        "comment" : "Continue tes efforts"
    },
    "Marianne" : {
        "note" : 10,
        "comment" : "tous juste la moyenne"
    },
    "Olivier" : {
        "note" : 16,
        "comment" : "Bon travail"
    }
}

# Récupérer la valeur du commentaire dans le directory inseré dans le directory
print(classe["Théo"]["comment"])

for eleve in classe:
    print(f"{eleve} à une note de {classe[eleve]['note']} et voici son appréciation : {classe[eleve]["comment"]}.")

# Ajouter un element dans le dictionnary (ajouter a la suite)

classe["Léa"] = {
    "note" : 17,
    "comment" : "très bon travail"
}

for eleve in classe:
    print(f"{eleve} à une note de {classe[eleve]['note']} et voici son appréciation : {classe[eleve]["comment"]}.")

# modifer une valeur dans le directory
classe["Olivier"]["note"] = 10
print(classe["Olivier"]["note"])

# supprimer un eleve
del classe["Marianne"]
for eleve in classe:
    print(eleve)

# verifier si un eleve existe dans le directory
if "Théo" in classe.keys():
    print("Théo est bien présent.")

# Sauvegarder les données de notre classe de façon persistante, au format Json
# import le module "json" (JavaScript Objet Notation)
with open('classe.json', 'w+') as file:

    #method de json: injecter mon dictionnary "classe" dans ce fichier
    json.dump(classe, file)

# au lieu de l'initialisé sur ce fichier, on vas aller charger et lire le fichier "classe.json" les informartions pour travailler dessus.
# voir le fichier use_json.py
