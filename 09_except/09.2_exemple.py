# Objectif :
# 1) afficher le contenue du fichier "bonjour.txt"
# 2) Faire un systeme de multiple exeption.

# Si le nom du fichier est incorrect, une erreur surviens.
# Pour eviter cela, on utilise le try/except

try:
    fichier = open('09_except/bonjour.txt')
    print(fichier.readlines()[9])
    fichier.close()

# except (FileNotFoundError, IndexError):
# On peut fait un except pour plusieur erreur.

# On peux utiliser plusieur except pour trouver le probleme:
except FileNotFoundError:
    print("Nom de fichier introuvable ou mal écrit.")
except IndexError:
    print("La ligne que tu veux afficher n'existe pas.")
finally:
# Code effectuer même si une erreur est attraper
    print("fini")
