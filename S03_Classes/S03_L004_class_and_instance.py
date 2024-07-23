class Car:
#zmienne definiowane na poziomie klasy a nie instancji klasy'
    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        Car.numberOfCars +=1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag  - ok      {}".format(self.isAirBagOK))
        print("Painting - ok      {}".format(self.isPaintingOK))
        print("Mechanic - ok      {}".format(self.isMechanicOK))
        print('-------------------------------')

print('Class level variables BEFORE creating instance:', Car.numberOfCars, Car.listOfCars)
car_01 = Car('Seta', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)
print('Class level variables AFTER creating instance:', Car.numberOfCars, Car.listOfCars)

print('Id of class is:', id(Car))
print('Id of instance are:', id(car_01),id(car_02))

print('Check if object belongs to class:', isinstance(car_01, Car))
print('Check if object belongs to class using type:', type(car_01) is Car)
print('Check class of an object using __clas__:', car_01.__class__)

print('List of instance attributes with values:', vars(car_01))
print('List of class attributes with values:', vars(Car))

print('List of instance attributes with dir:', dir(car_01))
print('List of class attributes with dir:', dir(Car))

print('Value taken from instance:', car_01.numberOfCars, 'Value taken from class', Car.numberOfCars)

Car.numberOfCars = 123
print('Value taken from instance:', car_01.numberOfCars, 'Value taken from class', Car.numberOfCars)


'''
car_01.GetInfo()
car_02.GetInfo()

print(car_01.brand, car_01.model, car_01.IsDamaged())
print(car_02.brand, car_02.model, car_02.IsDamaged())

print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK, car_01.isMechanicOK)
print(car_02.brand, car_02.model, car_02.isAirBagOK, car_02.isPaintingOK, car_02.isMechanicOK)
'''