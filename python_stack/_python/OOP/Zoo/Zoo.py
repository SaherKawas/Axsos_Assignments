from animals import *

class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name=zoo_name
        self.animals=[]

    def add_snake(self, name, age, gender, pattern, venomous):
        self.animals.append(Snake(name, age, gender, pattern, venomous))

    def add_sheep(self, name, age, gender, wool_color):
        self.animals.append(Sheep(name, age, gender, wool_color))

    def add_penguin(self, name, age, gender, married):
        self.animals.append(Penguin(name, age, gender, married))

    def add_bluewhale(self, name, age, gender, home_ocean):
        self.animals.append(Bluewhale(name, age, gender, home_ocean))

    def displayall_info(self):
        for a in self.animals:
            a.display_info()

zoo=Zoo("Ramallah Zoo")
zoo.add_snake("Black Mamba", 5, "female", "Dotted", True)
zoo.add_sheep("Shaun", 10, "female", "white")
zoo.add_penguin("Rico", 8, "male", False)
zoo.add_penguin("Skipper", 12, "male", True)
zoo.add_penguin("Private", 10, "male", False)
zoo.add_penguin("Kowalski", 7, "male", False)
zoo.add_bluewhale("Willy", 50, "male", "Atlantic")
zoo.displayall_info()
