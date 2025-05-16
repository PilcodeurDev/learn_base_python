import json

def read_json_file(file_name):
    try:
        #Si le nom de fichier NE se termine PAS en ".json"
        if not file_name.endswith(".json"):
            #Crée notre propre exeption
            raise Exception("Vous ne pouvez mettre que des fichier en .json")
        fichier = open(f'09_except/{file_name}')
        #readlines() pas adapter pour lire du json
        # print(fichier.readlines())
        #on import json pour lire du json
        #afficher juste la valeur de message -> ["message"]
        print(json.load(fichier))
        fichier.close()
    except Exception:
        print("erreur")
    except FileNotFoundError:
        print("Nom de fichier introuvable ou mal écrit.")

read_json_file("bonjour.txt")
