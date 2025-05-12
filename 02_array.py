from statistics import mean
from random import shuffle

# Creer une liste qui va stocker des pseudos pour simuler un jeux en ligne
# Exemple : Graven, Anana, Claymax...
online_players = ["Graven", "Anana", "Cleymax", "bob"]

print(online_players)
print(online_players[1])
print(online_players[len(online_players) - 1])

# Modifier "Graven" -> "Gravenilvec"
online_players[0] = "Gravaxident"
print(online_players)

# Ajouter une valeur entre "Anana" et "Cleymax"
online_players.insert(2, "BernardGamer34566")
print(online_players)

# Modifier plusieur valeurs a la fois
# Choisi a partir de quel valeur je souhaite modifier, le nombre de valeur.
online_players[2:4] = ["Paulette", "Marc"]
print(online_players)

# En ajouter d'autres en bout de liste
# Un joueur "Gamer1212" se connecte
online_players.append("Gamer1212")
online_players.extend(["Gogumerl", "Gifidu59"])
print(online_players)

# Anana se déconnecte
# soit del online_players[1]
# soit online_players.remove("Anana")
# soit
online_players.pop(1)
print(online_players)

# Suppression de tous les elements
online_players.clear()
print(online_players)

# La moyenne de notation d'élève
# Importer la méthode mean du module : statistics (en haut de la page)

notes = [
    8, 12, 10, 18, 4, 13, 11
]
print(notes)

result = mean(notes)
print("La moyenne de l'élève est de {}.".format(result))

# Changer l'ordre de façon aléatoire les notes dans le tableau
# -> from random import shuffle
shuffle(notes)
print(notes)


#créer une liste en découpant un string
text = input("Entrer une chaine de la forme suivante : email-pseudo-motdepasse. ").split("-")
print(text)

print("Salut {}, ton mail est : {} et voici ton mot de passe : {}".format(text[1], text[0], text[2]))

## Exercice : générateur de phrases
# Demander une chaine de la forme "mot1/mot2/mot3/...
# Transformer cette chaine de caractère en une liste
# La mélanger
# Si le nombre d'éléments de cette liste est inférieur à 10
# -> Afficher les deux premiers mots
# Si le nombre d'éléments est supérieur ou egal à 10
# -> Afficher les 3 derniers

# Demander une chaine de la forme "mot1/mot2/mot3/...
chained_words = input("Entrer une liste de mot au format mot1/mot2/mot3/... => ")

# Transformer cette chaine de caractère en une liste
word_list = chained_words.split("/")

# La mélanger
shuffle(word_list)

# Récuperer le nombre d'éléments
words_len = len(word_list)

# Si le nombre d'éléments de cette liste est inférieur à 10
if words_len < 10:
    # -> Afficher les deux premiers mots
    print(word_list[0:2])

# Si le nombre d'éléments est supérieur ou egal à 10
else:
    # -> Afficher les 3 derniers
    print(word_list[(words_len - 3):words_len])
