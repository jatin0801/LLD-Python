from abc import ABC, abstractmethod


# Vehicle interface
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Concrete vehicle classes
class Honda(Vehicle):
    def start(self):
        print("Honda Car is starting")

    def stop(self):
        print("Honda Car is stopping")


class Toyota(Vehicle):
    def start(self):
        print("Toyota Car is starting")

    def stop(self):
        print("Toyota Car is stopping")


class BMW(Vehicle):
    def start(self):
        print("BMW Car is starting")

    def stop(self):
        print("BMW Car is stopping")


# Abstract Factory Interface
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass


# Concrete Factories
class HondaFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Honda()


class ToyotaFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Toyota()


class BMWFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return BMW()


# Client Code
if __name__ == "__main__":
    honda_factory = HondaFactory()
    honda = honda_factory.create_vehicle()
    honda.start()
    honda.stop()

    toyota_factory = ToyotaFactory()
    toyota = toyota_factory.create_vehicle()
    toyota.start()
    toyota.stop()

    bmw_factory = BMWFactory()
    bmw = bmw_factory.create_vehicle()
    bmw.start()
    bmw.stop()
