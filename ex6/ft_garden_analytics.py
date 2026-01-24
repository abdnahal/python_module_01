class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, age, flower_color):
        super().__init__(name, height, age)
        self.flower_color = flower_color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, flower_color, prize_points):
        super().__init__(name, height, age, flower_color)
        self.prize_points = prize_points


class GardenManager:
    def __init__(self):
        self.gardens = {}

    def add_plant(self, name, plant):
        if name not in self.gardens.keys():
            self.gardens[name] = [plant]
            print(f"Added {plant.name} to {name}'s garden")

    ##def grow_all_plants(self, name):
        ##for i in self.gardens[name]: 


def main():
    dict = {'ahmed': [1, 2, 3], 'simo': [99, 88, 77], 'badr': [2, 7, 8]}
    print(dict['ahmed'])
    lst = dict['ahmed']
    for k in range(len(lst)):
        lst[k] += 1
    print(dict['ahmed'])

if __name__ == "__main__":
    main()