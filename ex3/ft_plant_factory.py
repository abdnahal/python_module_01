class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main():
    Plants = [
        ["Rose", 190, 78],
        ["Sunflower", 80, 30],
        ["Jassmin", 90, 25],
        ["Grass", 20, 180],
        ["herbes", 15, 27]]
    print("=== Plant Factory Output ===")
    for one in Plants:
        current = Plant(one[0], one[1], one[2])
        current.get_info()
    print()
    print(f"Total plants created: {len(Plants)}")


if __name__ == "__main__":
    main()
