class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale..")


class Fish(Animal):  # Fish inhertis from Animal
    def __init__(self):
        super().__init__()  # Call init of superclass (Animal)

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
