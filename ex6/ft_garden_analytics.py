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
    def __init__(self, name):
        self.name = name

    garden_count = 0

    def create_garden_network(self):
        self.gardens = dict()

    def create_garden(self, name):
        self.gardens[name] = []
        return self.gardens[name]

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

    def print_report(self, name):
        if name not in self.gardens:
            print(f"No garden found for {name}")
            return
        plants = self.gardens[name]
        print(f"{name}'s Garden has {len(plants)} plants")
        total = sum(p.height for p in plants)
        print(f"Total height: {total}cm")

    @staticmethod
    def validate_height(height):
        return height > 0

    def calculate_garden_score(self, garden_name):
        if garden_name not in self.gardens:
            return 0
        plants = self.gardens[garden_name]
        return len(plants) * 10 + sum(p.height for p in plants)

    @classmethod
    def total_gardens(cls):
        return 1

    class GardenStats:
        @staticmethod
        def plants_count(garden):
            return len(garden)

        @staticmethod
        def total_height(plants):
            total = 0
            for plant in plants:
                total += plant.height
            return total

        @classmethod
        def is_age(self, age):
            return age > 0

        @classmethod
        def is_height(self, height):
            return height > 0


def main():
    print("=== Garden Management System Demo ===")
    manager = GardenManager()
    manager.create_garden_network()

    alice_garden = manager.create_garden("Alice")
    bob_garden = manager.create_garden("Bob")

    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 100, "red")
    sunflower = PrizeFlower("Sunflower", 50, 36, "yellow", 10)

    manager.add_plant("Alice", oak)
    manager.add_plant("Alice", rose)
    manager.add_plant("Alice", sunflower)

    print("Alice is helping all plants grow...")
    manager.grow_all_plants("Alice")

    print("\n=== Alice's Garden Report ===")
    manager.print_report("Alice")

    print("\nHeight validation test:", GardenManager.validate_height(100))

    print("Garden scores - Alice and bob")
    manager.calculate_garden_score("Alice"),
    manager.calculate_garden_score("Bob")

    print(f"Alice's Garden: {alice_garden}")
    print(f"Bob's Garden: {bob_garden}")

    print("Total gardens managed:", GardenManager.total_gardens())


if __name__ == "__main__":
    main()
