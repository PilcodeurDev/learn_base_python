import json
# Charger et lire le fichier "classe.json" les informartions pour travailler dessus.

with open('classe.json', 'r') as file:
    classe = json.load(file)
    print(classe)
    file.close()

# On peut aller sur classe.json, modifier un element et il sera modifier sur ce fichier
