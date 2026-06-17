class Parrot:
    def __init__(self, name):
        self.name = name

    def sing(self):
        print(self.name, "can sing")

    def dance(self):
        print(self.name, "can dance")

bird = Parrot("Mithu")
bird.sing()
bird.dance()
