# class Animal:
#     def sound(self):
#         print("Generic animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("Woof Woof!")

# class Cat(Animal):
#     def sound(self):
#         print("Meow")

# animal = Animal()

# animal.sound()

# dog1 = Dog()

# dog1.sound()


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.make}, model: {self.model}, year: {self.year}")

    
class car(Vehicle):
    def __init__(self, make, model, year, body_model):
        super(.__init__(make, model, year)):
        self.body_model = body_model

class ElectricCar(car):
    def __init__(self, make, model, year, body_model, battery_capacity):
        super(.__init__(make, model, year, body_model))
        self.battery_capacity = battery_capacity
    def charge(self):
        print("Charging the electric car")


tesla = ElectricCar("Tesla", "Model X", 2023, "SUV", 122.4)

tesla.display_info()
print(telsa.body_model)
tesla.charge