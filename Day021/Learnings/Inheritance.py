class Animal:
    def __init__(self):
        self.no_of_eyes = 2

    def breath(self):
        print("Inhale and exhale")


class Fish(Animal):  # Fish class inherited from Animal class, obtaining properties like no of eyes and breath method
    def __init__(self):
        super().__init__()  # Initializing super class(Animal) Properties

    def breath(self):  # Overriding breath method from Animal class
        super().breath()
        print("Doing this under water")

    def swim(self):
        print("Moving in water")


fish = Fish()
print(fish.no_of_eyes)
fish.breath()
fish.swim()

animal = Animal()
animal.breath()

