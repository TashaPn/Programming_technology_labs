class House:
     def init(self):
        self.walls = 0
        self.roof = False
        self.windows = 0
         
class HouseBuilder:
    def __init__(self):
        self.house = House()
        
    def add_walls(self):
        self.house.walls = 4

    def add_roof(self):
        self.house.roof = True

    def add_windows(self):
        self.house.windows = 2

    def build(self):
        return self.house

a1 = HouseBuilder()
a1.add_walls()
a1.add_roof()
a1.add_windows()

house = a1.build()

print(house.walls)
print(house.roof)
print(house.windows)