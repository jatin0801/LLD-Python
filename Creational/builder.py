class Car:
    def __init__(self, builder):
        self.engine = builder.engine
        self.wheels = builder.wheels
        self.seats = builder.seats
        self.color = builder.color
        self.sunroof = builder.sunroof
        self.navigation_system = builder.navigation_system

    def get_engine(self):
        return self.engine

    def get_wheels(self):
        return self.wheels

    def get_seats(self):
        return self.seats

    def get_color(self):
        return self.color

    def has_sunroof(self):
        return self.sunroof

    def has_navigation_system(self):
        return self.navigation_system

    def __str__(self):
        return (f"Car [engine={self.engine}, wheels={self.wheels}, seats={self.seats}, "
                f"color={self.color}, sunroof={self.sunroof}, "
                f"navigation_system={self.navigation_system}]")

    class CarBuilder:
        def __init__(self):
            self.engine = None
            self.wheels = 4      # Default value
            self.seats = 5       # Default value
            self.color = "Black" # Default value
            self.sunroof = False
            self.navigation_system = False

        def set_engine(self, engine):
            self.engine = engine
            return self

        def set_wheels(self, wheels):
            self.wheels = wheels
            return self

        def set_seats(self, seats):
            self.seats = seats
            return self

        def set_color(self, color):
            self.color = color
            return self

        def set_sunroof(self, sunroof):
            self.sunroof = sunroof
            return self

        def set_navigation_system(self, navigation_system):
            self.navigation_system = navigation_system
            return self

        def build(self):
            return Car(self)

# example usage:
if __name__ == "__main__":
    car = (Car.CarBuilder(
    ).set_engine("V8")
    .set_color("Red")
    .set_sunroof(True)
    .build()
    )

    print(car)