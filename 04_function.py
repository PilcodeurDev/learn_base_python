# Définir une fonction en python, utilisation du mot clef : def + nom de la fonction (convention snake_case)

def welcome():
    print("Bienvenue sur ma chaine youtube")
    result = 5 + 6
    print("Le resultat de la valeur est ", result)

# Si je lance le script à ce moment la, rien ne ce passe puis que a aucun moment on appel la fonction ci dessus.

# Pour appeler la fonction, nommer la fonction :
#welcome()
# La fonction doit être appelé seulement après voir été créer

#year est une variable global, à l'inverse de locale, elle n'est pas dans la fonctiono u elle est appeler.
# Pour pouvoir l'utilisé dans notre fonction next_year(), nous devons l'importer dans la fonction avec le mot clef "global".
# Si elle n'est qu'utilise dans cette fonction , on peux la déplacer dans la fonction et l'utilisé en locale et non en globale/
year = 2018

def next_year():
    global year
    print("Fin de l'année", year)
    year += 1
    print("Débur de l'année", year)

next_year()
next_year()

# 2eme exemples :
# Sans le return dans la fonction, il n'y as pas de resultat envoi. Par conséquant le resultat est : "None"

def get_message():
    return "Le resultat de l'oprération est"

def get_none_message():
    "Le resultat de l'oprération est"

def addition_simple():
    result = 5 + 5
    return result

print(get_message(), addition_simple())

def multiply():
    return 5 * 8

print(get_none_message(), multiply())

# Répétition du code a divers endroit dans le code
# Mauvaise pratique (redondance)
def addition1():
    return 5 + 4

def addition2():
    return 5 + 6

def addition3():
    return 5 + 11

print("Le resultat est", addition1())
print("Le resultat est", addition2())
print("Le resultat est", addition3())

# Bonne pratique (clear)
# Permet de réutilisé la fonction deja créer en donnant un parametre ou argument "n", sans en créer une a chaque utilisation
# Obliger de donner un argument, possible de lui donner une valeur par défaut (n = 10). si on ne lui donne pas de valeur, 10 sera la valeur defaut
def addition(n = 10):
    return 5 + n

print("Le resultat est", addition(5))
print("Le resultat est", addition(6))
print("Le resultat est", addition())

#Exercice n°1 : Créer une fonction "max()" qui renvoi la valeur la plus haute parmis 2 chiffres différents entrer pas l'utilisateur.
def max(a, b):
    if a < b:
        return b
    else:
        return a

#first_number = int(input("Entrer votre premier nombre entier : "))
#second_number = int(input("Entrer votre deuxieme nombre entier : "))

#print("Voici le chiffre le plus grand", max(first_number, second_number))

#Exercice n°2 : créer une fonction pour calculer le nombre de voyelle dans un mot entrer par l'utilisateur
# Definir une fonction get_vowel_number()
# Créer un compteur de voyelles
# Pour chaque lettre, on vérifie si c'est une voyelle
# Si c'est une voyelle, on ajoute 1 au compteur
# On renvoi le resultat du compteur


# Definir une fonction get_vowel_number()
def get_vowel_number(user_word):

    # Créer un compteur de voyelles
    nb_vowel = 0
    # Liste des voyelles
    vowel_list = ["a", "e", "i", "o", "u", 'y']

    # Pour chaque lettre dans le mot de l'utilisateur, on vérifie si c'est une voyelle
    for letter in user_word:
        # Si c'est une voyelle, on ajoute 1 au compteur
        if letter in vowel_list:
            nb_vowel += 1
    # On renvoi le resultat du compteur
    return nb_vowel

# Input utilisateur
user_word = input("Veuillez entrez un mot pour connaitre le nombre de voyelle : ")

vowel_count = get_vowel_number(user_word)
print("Il y a", vowel_count, "voyelles dans le mot", user_word, ".")
