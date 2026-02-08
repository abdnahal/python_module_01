class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.days = age

    def age(self):
        self.days += 1

    def grow(self):
        self.height += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main():
    Sunflower = Plant("Sunflower", 250, 90)
    print("=== Day 1 ===")
    Sunflower.get_info()
    for i in range(1, 7):
        Sunflower.age()
        Sunflower.grow()
    print("=== Day 7 ===")
    Sunflower.get_info()
    print(f"Growth this week: +{i}cm")


if __name__ == "__main__":
    main()
