# Intercepter une ou plusieurs erreur pour eviter de faire cracher le programme

# # Calculer un prix TTC en partant de HT
# prixHT = int(input("Entrer votre prix Hors Taxe : "))
# prixTTC = prixHT * 1.2
# print(prixTTC)

# Si l'utilisateur rentre autre chose qu'un prix, on obtient une erreur.
# On essai d'attraper l'erreur avant quelle ne fasse planter le programme
# On utilise le mot clef : "try"
# executer une boucle infini tant que la personne ne met pas un nombre.
while True:
    try:
        prixHT = int(input("Entrer votre prix Hors Taxe : "))
        prixTTC = prixHT * 1.2
        print(prixTTC)
        break
    except ValueError:
        print("Une erreur est survenue.")
