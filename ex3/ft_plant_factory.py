class Plant :
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def get_info(self) :
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

def main():
    Plants = [
        ["Rose", 190, 78],
        ["Sunflower", 80, 30],
        ["Jassmin", 90, 25],
        ["Grass", 20, 180],
        ["herbes", 15, 27]]
    print("=== Plant Factory Output ===")
    k = 0
    for i in Plants:
        current = Plant(Plants[k][0], Plants[k][1], Plants[k][2])
        current.get_info()
        k += 1
    print()
    print(f"Total plants created: {k}")
    

if __name__ == "__main__":
    main()