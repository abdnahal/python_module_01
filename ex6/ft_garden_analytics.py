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
    @classmethod
    def garden

    class GardenStats:
        @staticmethod
        def plants_count(plant):
            return (len(plant))
        
        @staticmethod
        def total_height(plants):
            total = 0
            for plant in plants:
                total += plant.height
            return total
        
        @classmethod
        def is_age(age):
            return (age >= 0)
        
        @classmethod
        def is_age(height):
            return (height >= 0)

if __name__ == "__main__":
    
