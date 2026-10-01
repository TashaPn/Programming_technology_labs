from dataclasses import dataclass


@dataclass
class GameObject:

    Id : int
    Name : str
    x : int
    y : int


    def getId(self) -> int:        
        """
        возвращает идентификатор объекта
        """         
        return self.Id
    
    def GetName(self) -> str:  
        """
        возвращает имя объекта
        """            
        return self.Name

    def getX(self) -> int:  
        """
        возвращает значение где находится объект по X координате
        """              
        return self.x
        
    def getY(self) -> int:    
        """
        возвращает значение где находится объект по Y координате
        """           
        return self.y

    
@dataclass
class Unit(GameObject):

    alive : bool
    HP : float

    def getHP(self) -> float:
        """
        возвращает количество здоровья у юнита
        """
        return self.HP

    def isAlive(self):
        """
        возвращает, жив ли юнит
        """
        if self.HP > 0 :
            return True
        else:
            return False
    
    def receiveDamage(self, damage):
        """
        метод, который вызывается для получения урона этим юнитом
        """
        self.HP -= damage


@dataclass
class Building(GameObject):

    percent_build : int

    def isBuild(self):
        """
        возвращает, построена ли постройка или ещё нет
        """
        if self.percent_build == 100:
            return True
        else:
            return False


class Attacker:
    """
    Интерфейс Attacker
    """
    def attack(self, damage):
        """
        метод, принимающий юнит, которому наносится урон (как я поняла кол-во нанесённого урона)
        """
        return damage


class Movable:
    """
    Интерфейс Movable
    """
    def move(self):
        pass


class Archer(Unit, Attacker, Movable):
    pass


class Fort(Building, Attacker):
    pass


class MobileHome(Building, Movable):
    pass
  

"""
Что такое интерфейс в программировании ?
Интерфейс - это набор методов: которые торчат наружу
например, у класса А может быть 3 интерфейса

А.ленись() - интерфейс лентяй

А.вымирай() и А.ннака() - интерфейс вымирания

А.ешь() - интерфейс обеда


---


берем класс В

чтобы класс В соответствовал интерфейсу обеда, что надо сделать ?
надо, чтобы в классе В был метод ешь()

---

Class A:
    def ешь(селф):
        жру яблоки

Class B:
    def ешь(селф):
        ем тараканов

"""