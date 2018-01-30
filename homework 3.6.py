import random


class animals():
    def acceleration(self):
        self.speed = self.speed + 1

    def voice(self):
        print(self.language)

    def eat(self):
        self.satiety += 1

    def __init__(self):
        print("животное вызвано")


class cow(animals):
    speed = 0
    language = "мууу"
    milk = 0    #литры
    satiety = 0

    def recycling(self):
        if self.satiety > 0:
            self.satiety -= 1
            self.milk += 1
        else:
            print("вы слишком голодны")


class goat(animals):
    speed = 0
    language = "меее"
    satiety = 0
    health = 100
    self_evaluation = 20

    def fight_with_goat(self):
        losses = random.randrange(10, 20, 1)
        self.health -= losses
        exodus = random.random()
        if exodus == 0:
            self.self_evaluation += losses
        else:
            self.self_evaluation -= losses


class cheep(animals):
    speed = 0
    language = "меее"
    satiety = 0
    confidence = 0

    def get_lost(self):
        self.bewilderment -= 20

    def be_found(self):
        self.bewilderment += 20


class pig(animals):
    speed = 0
    language = "хрю-хрю"
    satiety = 0
    quantity_bugs = 200

    def lie_in_the_mud(self):
        self.quantity_bugs -= self.quantity_bugs*0,8


class duck(animals):
    speed = 0
    language =  "кря-кря"
    satiety = 0
    quantity_eggs = 0

    def take_down_the_eggs(self):
        egg = random.random(100, 300, 5)
        self.quantity_eggs += egg


class hens(animals):
    speed = 0
    language = "кудах-кудах"
    satiety = 0
    health = "alive"

    def escape(self):
        happening = random.random()
        if happening == 0:
            self.health = "alive"
            print("вы сбежали, побег удался")
        else:
            self.health = "death"
            print("в порыве к свободе вас поймали и зарубили")


class geese(animals):
    speed = 0
    language = "га-га-га"
    satiety = 0
    prick = 0

    def pinch_person(self):
        self.prick += 1
