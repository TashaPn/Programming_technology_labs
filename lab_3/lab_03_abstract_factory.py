class Cat:
    def speak(self):
        print("Мяу")

class Dog:
    def speak(self):
        print("Гав")

class CatFood:
    def show(self):
        print("Корм для кошки")

class DogFood:
    def show(self):
        print("Корм для собаки")

class AbstractFactory:
    def create_animal(self):
        pass
    def create_food(self):
        pass

class CatFactory(AbstractFactory):
    def create_animal(self):
        return Cat()
    def create_food(self):
        return CatFood()
    
class DogFactory(AbstractFactory):
    def create_animal(self):
        return Dog()
    def create_food(self):
        return DogFood()

    
a1 = CatFactory() 
a2 = DogFactory()

a1.create_animal().speak()
a1.create_food().show()

a2.create_animal().speak()
a2.create_food().show()