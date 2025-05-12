## Exercice : guichet de cinéma
# Recolter l'age de la personne.
# Si la personne est mineur
# Ajoute 7€ au total
# Si la personne est majeur
# Ajouter 9€ au total
# Demander si le client souhaitez du pop-corn.
# Si la réponse est "oui"
# Ajouter 5€ au total
# Affichez le prix

# Recolter l'age de la personne
age = int(input("Bonjour, quel age avez-vous ? "))
total = 0

# Si la personne est mineur
if age < 18:
    # Ajoute 7€ au total
    total += 7

# Si la personne est majeur
else:
    # Ajouter 9€ au total
    total += 9

# Demander si le client souhaitez du pop-corn.
bool_popcorn = input("Souhaitez-vous du popcorn ? ")

# Si la réponse est "oui"
if bool_popcorn == "oui":
    # Ajouter 5€ au total
    total += 5
    # Affichez le prix
    print("Cela fera {}€ s'il vous plait.".format(total))
    
else:
    # Affichez le prix
    print("Cela fera {}€ s'il vous plait.".format(total))
