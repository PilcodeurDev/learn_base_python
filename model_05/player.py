# un objet est un concept, un élement qui comporte une ou plusieurs caractéristiques.
# une arme est le moule (class) qui permet de créer plusieurs objets : pistolet, fusil, grenade, bazooka.
# on peux utilisé les caractéristiques suivantes : les dégats, la porté, nombre de munitions, etc...

# Moule permettant de représenté le concept de joueurs, ce par quoi il va être caractérisé.
class Player:

    # Les attributs caractérises le joueur
    # On se pose la question : "Qu'est ce qu'un joueur ?"
    # Exemple :
    # n°1 : le joueur est composé d'un pseudo
    # n°2 : le joueur est composé d'un nombre de point de vie
    # n°3 : le joueur est composé d'un nombre de point d'attaque

    #pseudo = "pilco"
    #health = 20
    #attack = 3

#Création d'une nouvelle INSTENCE de l'OBJET player
#player1 = Player()
#print("Bienvenue au joueur", player1.pseudo, "tu as", player1.health, "point de vie et", player1.attack, "point de dégats.")

# au lieu de créer un player en dure dans la class (ligne 15,16,17) nous allons créer le joueur en spécifiant ses attributs.

    # On appel ca le constructeur, c'est la premiere information initialisé lorsqu'on crée une nouvelle instance d'objet player.
    # (self) est une sorte de base de donnée propre à l'objet créer.
    # on y rajoute les attributs juste derriere que l'ont souhaite lui assigné (pseudo, health, attack).
    def __init__(self, pseudo, health, attack, weapon):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur", self.pseudo, "/ point de vie :", self.health, "/ point d'attaque :", self.attack, "et tu n'as pas d'arme.")
        pass

    # Nous allons pouvoir créer des methods : c'est une fonctions à l'interieur d'une class.
    # Ils en existent 3 différentes :

    # 1) Getter/ACCESSOR : Récupérer les informations
    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        if self.weapon != None:
            self.attack = self.weapon.damage
        return self.attack

    # 2) SETTER/MUTATEUR : Modifier des informations
    def damage(self, damage):
        self.health -= damage

    def set_weapon(self, weapon):
        self.weapon = weapon

    # 3) Les autres
    def attack_player(self, target_player):
        target_player.damage(self.attack)
