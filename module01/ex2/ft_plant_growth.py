print("=== Day 1 ===")

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def info(self):
        return f"{self.name.capitalize()}: {self.height}cm, {self.age} days old"

    def height_grow(self):
        self.height += 1

    def age_grow(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

plant = Plant("Rose", 2, 3)
plant.get_info()

start = plant.height

for _ in range(7):
    plant.age_grow()
    plant.height_grow()

print("=== Day 7 ===")
plant.get_info()

growth = plant.height - start
print(f"Growth this week: +{growth}cm")