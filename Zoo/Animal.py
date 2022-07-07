# animal is parent class 
class Animal:
    def __init__(self, name, age, health_level, happiness_level):
        pass
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level
# display_info method that shows the animal's name, health, and happiness.
    def display_info(self):
        print(f'the animal name is:{self.name},and health is : {self.health_level} and happiness {self.happiness_level}')
        return self
# a feed method that increases health and happiness by 10.
    def feed(self):
        self.health_level+=10
        self.happiness_level+=10 
        #print(f"the amount of health  is {self.health_level} and the amount of happines is {self.happiness_level}  ")
        return self
    def information(self):
        return self

# child class 
class Fish(Animal):
    def __init__(self, name):
        super().__init__(name, age=3, health_level=5, happiness_level=70)
        self.type = 'fish'
    def information(self):
        print(f"the name of animals is {self.name} and  type is {self.type} ")
# child class 
class Birds(Animal):
    def __init__(self, name):
        super(). __init__(name, age=60, health_level=66, happiness_level=77)
        self.type = 'birds'
        self.bird_color='black'
    def information(self):
        print(f"the name of animals is: {self.name} and  type is {self.type} and the color is: {self.bird_color}")
# child class 
class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name, age=22, health_level=100, happiness_level=55)
        self.type = 'tiger'
        self.life_span=10
        self.tiger_color='Yellow'
    def information(self):
        print(f"the animal name is:{self.name} and  type is {self.type} the {self.name} life span is:{self.life_span} ")



A = Tiger("Panthera Tigris Corbetti")
A.information()
