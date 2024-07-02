class Fish():
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def whoIAm(self):
        print(self.name)

class Shark(Fish):
    def a(self):
        print("a")

fish = Fish("aha", 5)
fish.whoIAm()
shark = Shark("aha1", 10)
shark.whoIAm()