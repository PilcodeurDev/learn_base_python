import json
# Exercice :
# Au lancement du programme, l'utilisateur à le choix entre plusieurs propositions :
# 1) afficher toutes les informations contenue dans le json (classe.json)
# 2) afficher les informations d'un elève
# 3) afficher la moyenne total de la classe
# 4) ajouter ou supprimer un nouvel elève

# Recuperer les informations du json dans une variable.
with open('classe.json', 'r') as file:
    classe = json.load(file)
    file.close()

def choice_user():
    print("Voici les actions disponibles.")
    print("")
    print("1. Voir les informations de tous les èleves.")
    print("2. Voir les informations d'un elève.")
    print("3. Afficher la moyenne total de la classe.")
    print('4. Ajouter un elève dans la classe.')
    print('5. Supprimer un elève de la classe.')
    print("")
    return input("Quel action souhaitez-vous faire ? ")

def show_student_list():
    print("Voici les elèves dans la classe :")
    for student in classe:
        print(f"- {student}")

print("Bonjour est bienvenue dans la base de donnée de votre classe.")

answer = choice_user()
print(f"Vous avez choisi l'action n°{answer}.")
print("")


if answer == "1":
# Afficher les informations de tous les èleves.
    print("Voici les informations des elèves :")
    for student in classe.items():
        print(student)

elif answer == "2":
    # Afficher les informations d'un elève.
    # Afficher la liste des eleves pour permettre le choix.
    show_student_list()
    # Demander quel elève vous souhaitez voir.
    print("")
    choice_student = input("De quel elève vous souhaitez les informations ? ")
    print("")
    for student in classe:
        if student == choice_student:
            print(f"{student} à une moyenne de : {classe[student]["note"]}/20. Voici le dernier commentaire reçu lors du bulletin trimestriel : {classe[student]["comment"]}.")

elif answer == "3":
    # Afficher la moyenne de la classe.
    general_average = 0
    for student in classe:
        general_average += int(classe[student]["note"])
    total = general_average / len(classe)
    print(f"La moyenne générale de la classe est de {total}/20 à ce trimestre.")

elif answer == "4":
    # Ajouter un elève à la classe.
    # Récuperer les informations de l'élève.
    name_student = input("Quel est le nom de l'élève à ajouter ? ")
    note_student = int(input("Quel est la moyenne de l'élève à ce trimestre ? "))
    comment_student = input("Quel est le commentaire pour l'élève à ce trimestre ? ")

    classe[name_student] = {
        "note" : note_student,
        "comment" : comment_student
    }
    with open('classe.json', 'w+') as file:
        json.dump(classe, file)

    show_student_list()

elif answer == "5":
    # Supprimer un élève à la classe.
    # Demaner quel élève supprimer.
    choice_student = input("Quel élève souhaitez-vous retirer de la base de donnée ? ")
    # si l'input existe, suppression de l'élève
    if choice_student in classe.keys():
        del classe[choice_student]
        with open('classe.json', 'w+') as file:
            json.dump(classe, file)
        print(f"Suppression de {choice_student} de la basse de donnée.")
        show_student_list()

else:
    answer = input("Je n'ai pas compris votre demande. Veuillez réécrire le chiffre de l'action souhaité.")
