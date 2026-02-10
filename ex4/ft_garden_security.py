class SecurePlant:
    def __init__(self, name, height, age):
        self.__name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {name}")

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_info(self):
        name = self.__name
        height = self.__height
        age = self.__age
        print(f"Current plant: {name} ({height}cm, {age} days)")


def main():
    print("=== Garden Security System ===")
    Rose = SecurePlant("Rose", 190, 25)
    Rose.set_age(17)
    Rose.set_height(180)
    print()
    Rose.set_age(-1)
    print()
    Rose.get_info()


if __name__ == "__main__":
    main()
