print("=== Plant Factory Output ===")

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

plant1 = Plant("Rose", 12, 3)
plant2 = Plant("Sunflower", 4, 1)

plant1.display()
plant2.display()

print("\nTotal plants created: 2")