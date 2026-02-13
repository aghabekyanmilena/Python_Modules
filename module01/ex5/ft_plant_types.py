print("=== Garden Plant Types ===")

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def info(self):
        return f"{self.name}: {self.height}cm, {self.age} days"

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def info(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age}, {self.color} color")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        area = self.trunk_diameter * 1.56
        print(f"{self.name} provides {area} meters of shade")

    def info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter} diameter")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")

    def nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

#flower
rose = Flower("Rose", 25, 30, "red")
tulip = Flower("Tulip", 20, 25, "yellow")

#tree
oak = Tree("Oak", 500, 1825, 50)
pine = Tree("Pine", 400, 1500, 40)

#vegetables
tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
carrot = Vegetable("Carrot", 30, 70, "autumn", "beta-carotene")

plants = [rose, tulip, oak, pine, tomato, carrot]

for plant in plants:
    plant.info()

print()

# Special behaviors
rose.bloom()
oak.produce_shade()
tomato.nutrition()

print("\nTotal plants created:", len(plants))


""" super() is a built-in Python function that allows a
child class to access methods of its parent class.
it is used to call the parent’s __init__() method.
gives access to the next class in the inheritance chain,
-> super() inside Flower refers to Plant.
-> lets child reuse and extend parent functionality without rewriting it
"""