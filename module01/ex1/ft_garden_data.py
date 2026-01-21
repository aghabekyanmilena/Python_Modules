print("=== Garden Plant Registry ===")

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def info(self):
        return f"{self.name.capitalize()}: {self.height}cm, {self.age} days old"

plant1 = Plant("rose", 12, 30)
plant2 = Plant("sunflower", 12, 30)
plant3 = Plant("cactus", 12, 30)

print(plant1.info())
print(plant2.info())
print(plant3.info())