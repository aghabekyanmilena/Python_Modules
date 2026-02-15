print("=== Garden Management System Demo ===")

class Plant():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew +1cm")

    def info(self):
        return (f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def info(self):
        status = "blooming" if self.blooming else "not blooming"
        return (f"{self.name}: {self.height}cm, {self.color} flower's {status}")

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def info(self):
        base_info = super().info()
        return (f"{base_info}, Prize points: {self.prize_points}")


# garden menegeric petqa sharunakem