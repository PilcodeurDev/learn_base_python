

#Exercice : Le juste prix
# Choisir un nombre entre 1 et 1000
# Tant que le prix n'as pas été trouvé par l'utilisateur
# Demander à l'utilisateur d'entrer le juste prix
# Si il trouve le juste prix le jeux s'arrete
# Sinon afficher "c'est plus" ou "c'est moins" pour l'aider à trouver le bon prix

# Instruction de départ du jeux
print("")
print("//////////////////////////////////////////////////////////")
print("Le Jeux du juste prix : Trouver le prix entre 1 et 1000.")
print("Top c'est parti !")
print("//////////////////////////////////////////////////////////")
print("")

# Choisir un nombre entre 1 et 1000
just_price = randint(1,1000)
print(just_price)

# récolte la valeur du joueur
player_price = int(input("Entrer un prix : "))

# Tant que le juste prix est différent de la valeur du joueur
while player_price != just_price:

    # Si la réponse est plus petite que le juste prix, annoncer "c'est plus".
    if player_price < just_price:
        print("C'est plus")

    # Si le joueur ce trombe en écrivant un chiffre au dela de 1000.
    elif player_price > 1000:
        print("Le prix est entre 0 et 1000.")

    # SI la réponse est plus grande que le juste prix, annoncer "c'est moins".
    else:
        print("C'est moins")

    print("")
    player_price = int(input("Entrer un nouveau prix : "))

# Jeu terminé, victoire du joueur
print("")
print("//////////////////////////////////////////////////////////")
print("Félicitations!! Vous avez trouvé le juste prix.")
print("//////////////////////////////////////////////////////////")
print("")
