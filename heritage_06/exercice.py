# Exercice d'héritage : Simulateur de ville
# Créer 3 classes : Immeuble, centre commercial, Banque
# Superclass : Batiment
# 4 immeubles, 2 centre commerciaux, 1 banque

class Building:
    def __init__(self, address, floor_nbr):
        self.address = address
        self.floor_nbr = floor_nbr
        pass

    def get_address(self):
        return self.address

    def get_floor_nbr(self):
        return self.floor_nbr

class Appartement_block(Building):

    def __init__(self, address, floor_nbr, balcony_nbr):
        super().__init__(address, floor_nbr)
        self.balcony_nbr = balcony_nbr
        print("Un nouvel immeuble à été créé au", self.address, "il a", self.floor_nbr, "étages et il possède", self.balcony_nbr, "balcons.")
        pass

    def get_balcony_nbr(self):
        return self.balcony_nbr

class Mall(Building):

    def __init__(self, address, floor_nbr, store):
        super().__init__(address, floor_nbr)
        self.store = store
        print("Un nouveau centre commercial à été créé au", self.address, "il a", self.floor_nbr, "étages et il possède", self.store, "magasins.")
        pass

    def get_store(self):
        return self.store

class Bank(Building):

    def __init__(self, address, floor_nbr, strongbox_nbr, name):
        super().__init__(address, floor_nbr)
        self.strongbox_nbr = strongbox_nbr
        self.name = name
        print("Une nouvelle banque du nom de", self.name, "à été créé au", self.address, "elle possède", self.floor_nbr, "étage et elle a", self.strongbox_nbr, "coffre-fort.")
        pass

    def get_strongbox_nbr(self):
        return self.strongbox_nbr

    def get_name(self):
        return self.name


# 4 immeubles
appartement_block1 = Appartement_block("30 place Clémenceau", 4, 21)
appartement_block2 = Appartement_block("24 rue de la Liberté", 3, 12)
appartement_block3 = Appartement_block("5 avenue Georges", 2, 4)
appartement_block4 = Appartement_block("1 place Goldman", 4, 19)

# 2 centre commerciaux
mall1 = Mall("4 avenue des Anglais", 2, 42)
mall2 = Mall("12 rue Montagnes", 3, 72)

# 1 banque
bank1 = Bank("12 avenue Général De Gaulle", 1, 43, "Cofidis")

#PS : Besoin de la notion suivante : les directory pour création en boucle.
