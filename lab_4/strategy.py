from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):

    @abstractmethod
    def calculate_cost(self):
        pass

class StandardDelivery(DeliveryStrategy):

    def calculate_cost(self):
        return 250

class ExpressDelivery(DeliveryStrategy):

    def calculate_cost(self):
        return 500

class PickupDelivery(DeliveryStrategy):

    def calculate_cost(self):
        return 0

class DeliveryCalculator:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self):
        return self.strategy.calculate_cost()



calculator = DeliveryCalculator(StandardDelivery())
print("Обычная доставка:", calculator.calculate(), "руб.")

calculator.set_strategy(ExpressDelivery())
print("Экспресс-доставка:", calculator.calculate(), "руб.")

calculator.set_strategy(PickupDelivery())
print("Самовывоз:", calculator.calculate(), "руб.")