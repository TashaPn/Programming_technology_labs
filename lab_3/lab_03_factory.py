class Cat:
    def speak(self):
        print("Мяу")


class Dog:
    def speak(self):
        print("Гав")


class Factory:
    def create(self):
        pass


class CatFactory(Factory):
    def create(self):
        return Cat()


class DogFactory(Factory):
    def create(self):
        return Dog()


a1 = CatFactory().create()
a2 = DogFactory().create()

a1.speak()
a2.speak()