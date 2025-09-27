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
class Car(Vehicle):
    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")


class Truck(Vehicle):
    def start(self):
        print("Truck is starting...")

    def stop(self):
        print("Truck is stopping...")


class Bike(Vehicle):
    def start(self):
        print("Bike is starting...")

    def stop(self):
        print("Bike is stopping...")


# Factory class
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type: str) -> Vehicle:
        if vehicle_type == "Car":
            return Car()
        elif vehicle_type == "Truck":
            return Truck()
        elif vehicle_type == "Bike":
            return Bike()
        else:
            raise ValueError("Unknown vehicle type")


# Client code (Main)
if __name__ == "__main__":
    vehicle1 = VehicleFactory.get_vehicle("Car")
    vehicle1.start()
    vehicle1.stop()

    vehicle2 = VehicleFactory.get_vehicle("Truck")
    vehicle2.start()
    vehicle2.stop()

    vehicle3 = VehicleFactory.get_vehicle("Bike")
    vehicle3.start()
    vehicle3.stop()
