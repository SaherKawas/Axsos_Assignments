from Animal import Animal

class Snake(Animal):
    def __init__(self, name, age, gender, pattern, venomous):
        super().__init__(name, age, gender, 25)
        self.pattern=pattern
        self.venomous=venomous
        
    def display_info(self):
        print(f"{self.name}: age:{self.age}, health:{self.health}/{self.max_health} happiness:{self.happiness}, pattern:{self.pattern}, venomous:{self.venomous}")


class Sheep(Animal):
    def __init__(self, name, age, gender, wool_color):
        super().__init__(name, age, gender, 70)
        self.wool_color=wool_color
       
        
    def display_info(self):
        print(f"{self.name}: age:{self.age}, health:{self.health}/{self.max_health} happiness:{self.happiness}, Wool color:{self.wool_color}")


class Penguin(Animal):
    def __init__(self, name, age, gender, married):
        super().__init__(name, age, gender, 30)
        self.married=married
       
        
    def display_info(self):
        print(f"{self.name}: age:{self.age}, health:{self.health}/{self.max_health} happiness:{self.happiness}, Married:{self.married}")


class Bluewhale(Animal):
    def __init__(self, name, age, gender, home_ocean):
        super().__init__(name, age, gender, 1000)
        self.home_ocean=home_ocean
       
        
    def display_info(self):
        print(f"{self.name}: age:{self.age}, health:{self.health}/{self.max_health} happiness:{self.happiness}, Home Ocean:{self.home_ocean}")




