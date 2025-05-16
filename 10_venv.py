# Ce qu'il faut savoir :

# Moyen simple en python d'embarquer sa propre configuration : toute les dépendances ainsi que leurs verisons.

# La problématique est la suivante :
#
# Imaginons que vous avez un projet (ex : site internet) avec un module au hasard : flask. Ce module est installé sur la version python qui est sur ma machine.
# Mais si déplace le site sur une autre machine ou un serveur, je vais devoir re installer manuellement cette version de flask. Donc grosse perte de temps et possibilité de faire des erreurs.
# Cest pour cela qu'on utilise des "venv".



## 1) Créer un venv dans ton terminal :
# python3 -m venv myenv
# La commande crée un nouveau dossier à l'interieur de votre programme
#
#
# a) Actier l'environnement virtuel
#
# Activer sur windows : ./myenv/Scripts/activate
# Activer sur mac : source ./myenv/bin/activate
#
# Vérification : Le préfixe sur le terminal devient (myenv)
# (tous ce qui sera fait dans le terminal restera dans l'environnement virtuel)
#
#
# b)désactiver l'environnement virtuel
# Désactiver sur mac/windows : deactivate
#
# Vérification : Le préfixe est retiré



## 2) Installation de module (ex : flask + python-dotenv)
#
# Commande : pip(3?) install flask python-dotenv
#
# Vérification : python3 nom_programme.py



## 3) Geler ses dépendances pour les stocker
#
# Commande de création : pip(3?) freeze > requirements.txt
#(convention de nomage = requirements.txt)
#
# Crée un fichier avec la liste de toute les dépendances ainsi que leur version permettant de tous réinstaller correctement sur nimporte quelle machine/serveur.
#
# Commande d'installation : pip(3?) install -r requirements.txt
