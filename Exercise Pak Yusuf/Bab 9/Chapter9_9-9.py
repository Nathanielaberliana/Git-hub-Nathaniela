class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"Mobil ini sudah menempuh {self.odometer_reading} mil.")


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini punya baterai {self.battery_size}-kWh.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"Mobil ini bisa menempuh sekitar {range} mil dengan baterai penuh.")

    def upgrade_battery(self):
        """Naikkan kapasitas baterai ke 65 kalau belum 65."""
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_car = ElectricCar('tesla', 'model s', 2024)
print(my_car.get_descriptive_name())

my_car.battery.get_range()

my_car.battery.upgrade_battery()
my_car.battery.get_range()