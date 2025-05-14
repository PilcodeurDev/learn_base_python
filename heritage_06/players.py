class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur", self.pseudo, "/ point de vie :", self.health, "/ point d'attaque :", self.attack, "et tu n'as pas d'arme.")
        pass

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        target_player.damage(self.attack)


# Création d'une nouvelle class warrior avec une nouvelle caractéristique : armor
# Warrior est parenté à Player car elle à les même caractéristiques, avec des spécialisations en plus.
# Warrior est l'élement enfant, player l'élement parent.
# donc on peux rajouter "(Player)" collé au model de la class Warrior pour expliqué son lien de parenté.
# On va uniquement garder les caractéristiques spécifiques au Warrior.
# Une class enfant peu avoir plusieurs class parents.
class Warrior(Player):



    def __init__(self, pseudo, health, attack):
        #les caractéristiques pseudo, health et attack sont stocker nul par.
        # Donc il faut appelé le constructeur du parent Player pour construire l'élément enfant Warrior.
        #mot clef : super() pour appelé le constructeur parent de Player, avec les caractéristiques.
        super().__init__(pseudo, health, attack)
        #peu etre aussi ecrit en dur comme ceci
        self.armor = 3
        print("Bienvenue au guerrier", self.pseudo, "/ point de vie :", self.health, "/ point d'attaque :", self.attack)
        pass

    def get_armor_point(self):
        return self.armor

    def damage(self, damage):
        #armor viens changer la mécanique de dégat
        if self.armor > 0:
            self.armor -= 1
            damage = 0
        #Warrior modifie la method de base de Player
        #On recupère la method de Player avec super()
        super().damage(damage)

        self.health -= damage

    #recharge les points d'armure du warrior, en les repassant à 3.
    def blade(self):
        self.armor = 3
        # Les print ne sont pas sensé être ecrit ici, c'est pour nous comprendre l'exemple
        print("Les points d'armures ont été rechargés.")

warrior1 = Warrior("Tsubaky", 30, 4)
warrior1.damage(4)
print(warrior1.get_health(), "armure :", warrior1.get_armor_point())

# issubclass() permet de vérifié si la class enfant est bien relier a la class parent.
if issubclass(Warrior, Player):
    print("Le guerrier est bien une spécialisation du Joueur")
