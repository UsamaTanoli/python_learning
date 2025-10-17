class Car:
   total_cars = 0

   def __init__(self, brand, model):
      self.__brand = brand
      self.model = model
      Car.total_cars += 1

   def full_name(self):
      return f"Brand name is: '{self.__brand}' and Model name is: '{self.model}'"

   def get_brand(self):
      return self.__brand + "!"
   
   def set_brand(self, new_brand):
      self.__brand = new_brand

   def fuel_type(self):
      return "Petrol Or Diesel"



class ElectricCars(Car):
   def __init__(self, brand, model, battery_size):
      super().__init__(brand, model)
      self.battery_size = battery_size

   def fuel_type(self):
      return "Electric Charge"


# my_car = Car("Toyota", "LC300")
# print(my_car.brand)
# print(my_car.model, "\n")


# my_second_car = Car("BMW", "X7")
# print(my_second_car.brand)
# print(my_second_car.model)

# print(my_car.full_name())

# electric_car = ElectricCars("Tesla", "Model S Plaid", "100.0 kWh")
# print(electric_car.brand)
# print(electric_car.model)
# print(electric_car.battery_size)
# print(electric_car.full_name())
# print(electric_car.get_brand())
# print(electric_car.__brand)

## After setter func
# electric_car.set_brand("lucid")
# print(electric_car.get_brand())


# polymorphism

# print(my_car.fuel_type())
# print(electric_car.fuel_type())


#printing total cars 
# fav_car1 = Car("Toyota", "LC200")
# fav_car2 = Car("Lexus", "LX570")
# fav_car1 = Car("Toyota", "LC300")
# print(Car.total_cars)