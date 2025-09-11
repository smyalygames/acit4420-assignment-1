class ElectricCar:
    def fuel_type(self):
        return "Electric"
class GasCar:
    def fuel_type(self):
        return "Gasoline"
class HybridCar(ElectricCar, GasCar):
    pass
car = HybridCar()
print(car.fuel_type())