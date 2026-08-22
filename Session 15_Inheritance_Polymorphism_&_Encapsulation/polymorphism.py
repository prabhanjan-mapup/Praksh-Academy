class Animal:
    def __init__(self,name):
        self.name = name

    def soundOfAnimal(self):
        print("Sample")

class Dog(Animal):
    def soundOfAnimal(self):
        print("Bow Bow")

class Cat(Animal):
    def soundOfAnimal(self):
        print("Meow Meow")

dog = Dog("Dog")
dog.soundOfAnimal()

cat = Cat("Cat")
cat.soundOfAnimal()