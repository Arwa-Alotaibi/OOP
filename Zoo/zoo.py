from Animal import Animal
from Animal import Birds
from Animal import Fish
from Animal import Tiger 
class zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_tiger(self, name):
        self.animals.append(Tiger(name) )
    def add_birds(self, name):
        self.animals.append(Birds(name) )
    def add_fish(self, name):
        self.animals.append(Fish(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

Zoo1 = zoo("John's Zoo")
Zoo1.add_tiger("Panthera Tigris Corbetti")
Zoo1.add_birds('Gamebirds')
Zoo1.add_fish('Atlantic Cod')
Zoo1.print_all_info()