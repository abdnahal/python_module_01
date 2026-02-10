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


class GardenManager():
    def __init__(self):
        pass

    def create_garden_network(self):
        self.gardens = dict

    def create_garden(self, name):
        self.gardens[name] = []

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


def main():
    print("=== Garden Management System Demo ===")

    # Create manager using class-level constructor
    manager = GardenManager.create_garden_network()

    # Create gardens
    alice_garden = manager.create_garden("Alice")
    bob_garden = manager.create_garden("Bob")

    # Create plants (inheritance chain)
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    # Add plants
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    # Grow plants (instance method test)
    print("Alice is helping all plants grow...")
    alice_garden.grow_all()

    # Generate report using nested GardenStats
    print("\n=== Alice's Garden Report ===")
    alice_garden.print_report()

    # Static utility function test
    print("\nHeight validation test:",
          GardenManager.validate_height(100))

    # Compare gardens (class-level analytics)
    print("Garden scores - Alice:",
          manager.calculate_garden_score(alice_garden),
          ", Bob:",
          manager.calculate_garden_score(bob_garden))

    # Class method counter
    print("Total gardens managed:",
          GardenManager.total_gardens())


if __name__ == "__main__":
    main()
