from dataclasses import dataclass
from abc import ABC, abstractmethod


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

    def isAlive(self) -> bool:
        """
        возвращает, жив ли юнит
        """
        if self.HP > 0 :
            return True

        return False
    
    def receiveDamage(self, damage: float):
        """
        метод, который вызывается для получения урона этим юнитом
        """
        self.HP -= damage


@dataclass
class Building(GameObject):

    percent_build : int

    def isBuild(self) -> bool:
        """
        возвращает, построена ли постройка или ещё нет
        """
        if self.percent_build == 100:
            return True

        return False


class Attacker(ABC):
    """
    Интерфейс Attacker
    """
    @abstractmethod
    def attack(self, unit: Unit):
        """
        метод, принимающий юнит, которому наносится урон
        """


class Movable(ABC):
    """
    Интерфейс Movable
    """
    @abstractmethod
    def move(self):
        """
        метод, обеспечивающий движение
        """


class Archer(Unit, Attacker, Movable):
    def attack(self, unit: Unit):
        """
        Реализация абстрактного метода
        """
        pass

    def move(self):
        """
        Реализация абстрактного метода
        """
        pass


class Fort(Building, Attacker):
    def attack(self, unit: Unit):
        """
        Реализация абстрактного метода
        """
        pass


class MobileHouse(Building, Movable):
    def move(self):
        """
        Реализация абстрактного метода
        """
        pass
  




