# for : pour une valeur de départ, jusqu'à une valeur de fin.
# Attention: la derniere valeur est TOUJOURS exclus.
# donc pour afficher le message à 10 clients -> range(1,11)
for num_client in range(1, 6):
    print("Vous êtes le client n°", num_client)

# for each : pour chaque valeur d'une liste données
# Lister les emails
emails = ["gravenilvac@gmail.com", "graven@hotmail.com", "coucou@free.com", "oldenpaso@jose.es", "pierredupont@gmail.yt"]

# Blacklister certain email
blacklist = ["gravenilvac@gmail.com", "graven@hotmail.com"]

# Pour chaque valeur, j'affiche le message
for email in emails:

    if email in blacklist:
        print("Email {} interdit : envoi impossible...".format(email))
        #mot clef : "continue" permet de finir l'itération actuelle et passer à la suivante
        #mot clef : "break" permet de stopper la boucle avec toute ses itérations restantes
        continue

    print("Email envoyé à :", email)

# while : tant qu'une condition est vrai
# Exemple n°1 :

# salarié gagne 1500€ / mois
salary = 1500

# tant que le salaire < 2000€, prime de 120€/mois

while salary < 2000:
    salary += 120
    print("Votre salaire actuelle est de ", salary, "€")

print("Fin du programme")

# Exemple n°2 :
# un youtubeur "Pilco" à 2500 abonnées
suscribers_count = 2500

# Il gagne 10% d'abonnées par mois
months = 0

# Combien aura t'il d'abonnées dans deux ans ?
while months < 24:
    # Incrémenter la valeurs months de 1 a chaque itération
    months += 1
    # Augmenter de 10% l'audience
    suscribers_count *= 1.1
    # Utiliser des chiffres rond pour afficher l'évolution dans la console
    int_count = "{:.0f}".format(suscribers_count)
    print("Cela fait {} mois et le nombre d'abonnés est passé à {}".format(months, int_count))
# Résultat au bout de deux ans.
print("J'ai atteint {} abonnés au bout de deux ans.".format(int_count))
