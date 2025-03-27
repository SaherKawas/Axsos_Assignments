class Animal:
    def __init__(self, name, age, gender, max_health=100):
        self.name=name
        self.age=age
        self.gender=gender
        self.health=max_health
        self.happiness=100
        self.max_health=max_health
        
    
    def display_info(self):
        print(f"{self.name}: age:{self.age}, health:{self.health}\{self.max_health} happiness:{self.happiness}")

    def feed(self):
        self.health+=10
        self.happiness+=10
        if self.health>self.max_health:self.health=self.max_health
        if self.happiness>100:self.happiness=100