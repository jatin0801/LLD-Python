from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def getDesctiption(self):
        pass
    @abstractmethod
    def getCost(self):
        pass


class FilterCoffee(Coffee):
    def getDesctiption(self) -> str:
        return "Filter Coffee"
    def getCost(self) -> float:
        return 4.0
    
class FrenchCoffee(Coffee):
    def getDesctiption(self) -> str:
        return "French Coffee"
    def getCost(self) -> float:
        return 5.0
    
class IraniCoffee(Coffee):
    def getDesctiption(self) -> str:
        return "Irani Coffee"
    def getCost(self) -> float:
        return 2.0
    
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @abstractmethod
    def getDesctiption(self) -> str:
        return self._coffee.getDesctiption()

    @abstractmethod
    def getCost(self) -> float:
        return self._coffee.getCost()

class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def getDesctiption(self) -> str:
        return super().getDesctiption() + " + Milk"
    
    def getCost(self):
        return super().getCost() + 1.5

class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee) 

    def getDesctiption(self) -> str:
        return super().getDesctiption() + " + Sugar"
    
    def getCost(self):
        return super().getCost() + 0.5

class CreamDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def getDesctiption(self) -> str:
        return super().getDesctiption() + " + Cream"
    
    def getCost(self):
        return super().getCost() + 0.25
    
def main():
    jatin_coffee = FilterCoffee()
    print("Normal Coffee")
    print(jatin_coffee.getDesctiption())
    print(jatin_coffee.getCost())
    print("Coffee with add ons")
    jatin_coffee = CreamDecorator(jatin_coffee)
    jatin_coffee = SugarDecorator(jatin_coffee)
    print(jatin_coffee.getDesctiption())
    print(jatin_coffee.getCost())

    dimple_coffee = IraniCoffee()
    dimple_coffee = MilkDecorator(dimple_coffee)
    dimple_coffee = SugarDecorator(dimple_coffee)
    print(dimple_coffee.getDesctiption())
    print(dimple_coffee.getCost())

if __name__ == "__main__":
    main()