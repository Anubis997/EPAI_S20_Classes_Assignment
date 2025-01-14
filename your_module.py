import datetime

class Person:
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self._birth_year = birth_year
        self.base_salary = 50000
        self._bonus = 10

    @property
    def age(self):
        current_year = datetime.datetime.now().year
        return current_year - self._birth_year

    def set_birth_year(self, year):
        self._birth_year = year

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split()
        self.first_name = first
        self.last_name = last

    @property
    def salary(self):
        return self.base_salary + (self.base_salary * self.bonus / 100)

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Bonus must be between 0 and 100.")
        self._bonus = value

    @property
    def current_year(self):
        return datetime.datetime.now().year

class Circle:
    def __init__(self, radius=0):  # Initialize with a default radius of 0
        self._radius = None
        self.radius = radius  # Use the setter for validation
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be a positive number.")
        self._radius = value
        self._area = None  # Invalidate cached area

    @property
    def diameter(self):
        return self.radius * 2  # This will work because radius is initialized properly

    @property
    def area(self):
        if self._area is None:
            import math
            self._area = math.pi * (self.radius ** 2)
        return self._area


class Vehicle:
    vehicle_count = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Vehicle.vehicle_count += 1

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count

    @staticmethod
    def classify_vehicle(vehicle_type):
        return f"This is a {vehicle_type}"

class ElectricVehicle(Vehicle):
    @staticmethod
    def classify_vehicle(vehicle_type):
        return f"This is an electric {vehicle_type}"

class DynamicClass:
    static_value = "I am static"

    def __init__(self):
        pass

    def dynamic_attr(self, name, value):
        setattr(self, name, value)

class ValidatedAttribute:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("Value must be a positive integer.")
        self._value = value
