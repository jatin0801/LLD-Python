from abc import ABC, abstractmethod

class SmartComponent(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class SmartBulb(SmartComponent):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def turn_on(self):
        print("Turning ON SmartBulb...", self.name)
    
    def turn_off(self):
        print("Turning OFF SmartBulb...", self.name)

class SmartFan(SmartComponent):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def turn_on(self):
        print("Turning ON SmartFan...", self.name)
    
    def turn_off(self):
        print("Turning OFF SmartFan...", self.name)

class SmartAC(SmartComponent):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def turn_on(self):
        print("Turning ON SmartAC...", self.name)
    
    def turn_off(self):
        print("Turning OFF SmartAC...", self.name)

class CompositeSmartComponent(SmartComponent):
    def __init__(self, name):
        self._components : list[SmartComponent] = []
        self.name = name
        print("Initializing... ", name)

    def add_component(self, component: SmartComponent):
        self._components.append(component)
        print(f"added {component.name} in {self.name}")


    def remove_component(self, component: SmartComponent):
        self._components.remove(component)
        print(f"removed {component.name} from {self.name}")

    def turn_on(self):
        print(f"turning ON {self.name}")
        for sc in self._components:
            sc.turn_on()
    
    def turn_off(self):
        print(f"turning OFF {self.name}")
        for sc in self._components:
            sc.turn_off()

if __name__ == "__main__":
    house = CompositeSmartComponent("house")
    floor1 = CompositeSmartComponent("floor 1")
    floor2 = CompositeSmartComponent("floor 2")

    house.add_component(floor1)
    house.add_component(floor2)

    floor1.add_component(SmartAC("AC1"))
    floor1.add_component(SmartAC("AC2"))
    floor1.add_component(SmartBulb("Bulb1"))
    floor1.turn_on()
    floor1.turn_off()

    
    floor2.add_component(SmartFan("Fan1"))
    floor2.add_component(SmartFan("Fan2"))
    floor2.add_component(SmartFan("Fan3"))
    floor2.add_component(SmartBulb("Bulb1"))
    floor2.add_component(SmartBulb("Bulb2"))
    floor2.add_component(SmartBulb("Bulb3"))
    floor2.turn_on()

    print("I'm leaving. lets turn off everything!!!")
    house.turn_off()
    