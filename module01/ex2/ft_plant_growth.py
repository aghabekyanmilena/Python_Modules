print("=== Garden Plant Registry ===")

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def info(self):
        return f"{self.name.capitalize()}: {self.height}cm, {self.age} days old"
    # def grow(self):