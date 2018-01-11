class Farm():
    animals = {"cow": 0, "goat": 0, "cheep": 0, "pig": 0 }
    birds = {"duck": 0, "hens": 0, "geese": 0 }

    def change_quantity(self, being, quantity, class_ = animals):
        self,class_[being] = quantity


    def change_quantity_foot(self, quantity):
        self.quantity_foot = int(quantity)

class animals(Farm):
    animals_collor = {"cow": "white", "goat": "gray", "cheep": "green", "pig": "pink"}
    quantity_foot = 4
    def change_collor(self, animal, collor):
        self.animals_collor[animals] = collor

class birds(Farm):
    birds_collor = {"duck": "white", "hens": "brown", "geese": "white"}
    quantity_foot = 4
    def change_collor(self, birds, collor):
        self.birds_collor[birds] = collor