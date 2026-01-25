class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def main():
    Jassmin = Plant("Jassmin", 190, 25)
    Corn = Plant("Corn", 90, 15)
    Sunflower = Plant("Sunflower", 250, 90)
    all = [Jassmin, Corn, Sunflower]
    print("=== Garden Plant Registry ===")
    for i in range(3):
        print(f"{all[i].name}: {all[i].height}cm, {all[i].age} days old")


if __name__ == "__main__":
    main()
