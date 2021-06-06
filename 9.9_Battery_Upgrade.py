import time


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        full_name = f'{self.year} {self.make} {self.model}'
        return full_name.title()

    def read_odometer(self):
        print("This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank():
        print("This car doesn't need a gas tank!")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a {self.battery_size} -kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        mess = f"This car can go approximately {range} miles on a full charge"
        return mess

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


def main():
    car = ElectricCar('tesla', 'model s', 2016)
    print(car.get_descriptive_name())
    print(car.battery.get_range())
    car.battery.upgrade_battery()
    print("After increase...")
    time.sleep(1)
    print(car.battery.get_range())


if __name__ == '__main__':
    main()
