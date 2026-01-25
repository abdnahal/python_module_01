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
            self.gardens[name] = []
        self.gardens[name].append(plant)
        print(f"Added {plant.name} to {name}'s garden")

    def grow_all_plants(self, name):
        if name not in self.gardens:
            print(f"{name} has no gardens!")
            return

        print(f"{name} is helping all plants grow...")
        for plant in self.gardens[name]:
            plant.grow()


if __name__ == "__main__":
    main()
