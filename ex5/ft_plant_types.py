class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def status(self):
        name = self.name
        height = self.height
        age = self.age
        print(f"{name} (Flower): {height}cm, {age} days, {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def status(self):
        diameter = self.trunk_diameter
        name = self.name
        height = self.height
        age = self.age
        print(f"{name} (Tree): {height}cm, {age} days, {diameter}cm diameter")

    def produce_shade(self):
        shade = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def status(self):
        name = self.name
        height = self.height
        age = self.age
        season = self.harvest_season
        print(f"{name} (Vegetable): {height}cm, {age} days, {season} harvest")
        print(f"{name} is rich in {self.nutritional_value}")


def main():
    print("=== Garden Plant Types ===")
    print()
    Rose = Flower("Rose", 30, 25, "Yellow")
    Rose.status()
    Rose.bloom()
    print()
    Oak = Tree("Oak", 500, 99, 50)
    Oak.status()
    Oak.produce_shade()
    print()
    Potato = Vegetable("Potato", 200, 33, "Winter", "Protein")
    Potato.status()


if __name__ == "__main__":
    main()
