from model_05.player import Player
from model_05.weapon import Weapon

player1 = Player("Pilco", 20, 3, None)
player2 = Player("Tsubaky", 18, 5, None)

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo(), "et lui retire", player1.get_attack(), "point de vie.")

knife = Weapon("Couteau", 10)

player1.set_weapon(knife)
print(player1.get_pseudo(), "a ramasser un couteau, ses points de dégats son passer à", player1.get_attack())
