class LandAnimal:
    def __init__(self):
        super().__init__()
        self.walking_speed=5


class WaterAnimal:
    def __init__(self):
        super().__init__()
        self.swimming_speed=10


class Amphibian(WaterAnimal,LandAnimal):
    def __init__(self):
        super().__init__()

a=Amphibian()
print(a.walking_speed)
print(a.swimming_speed)
