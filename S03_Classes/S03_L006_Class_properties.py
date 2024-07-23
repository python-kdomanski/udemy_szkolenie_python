class Car:
#zmienne definiowane na poziomie klasy a nie instancji klasy'
    numberOfCars = 0
    listOfCars = []


    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale  #jak zaczyna się od __ to oznacza że jest to wewnętrzme/ukryte
        Car.numberOfCars +=1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag  - ok      {}".format(self.isAirBagOK))
        print("Painting - ok      {}".format(self.isPaintingOK))
        print("Mechanic - ok      {}".format(self.isMechanicOK))
        print("Is on sale         {}".format(self.__isOnSale))
        print('-------------------------------')

print('Class level variables BEFORE creating instance:', Car.numberOfCars, Car.listOfCars)
car_01 = Car('Seta', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)
print('Class level variables AFTER creating instance:', Car.numberOfCars, Car.listOfCars)

car_02.__isOnSale = False #ukryta/wewnętrzna więc się nie uda zmienić wartości, ple bez __ udało by się

car_02._Car__isOnSale = False # tu się udaje zminić - niestety klasy w Python nie bronią się przed zewnętrzną modyfikacją pól

car_02.YearOfProduction = 2005 #doda nowy atrybut do klasy
del car_02.YearOfProduction #to usuwa atrybut z klasy
#W python klasy można modyfikować w czasie życia obiektu - inaczej jak w C# i innych

setattr(car_02, 'TAXI',False) #pozwala dodać nowy atrybut do klasy
print(hasattr(car_02,'TAXI')) #hasattr pozwala sprawdzić czy klasa posoada zadany atrybut
delattr(car_02,'TAXI') #delattr usuwa atrybut z klasy - tak sama jako del
print(hasattr(car_02,'TAXI')) #hasattr pozwala sprawdzić czy klasa posoada zadany atrybut

car_01.GetInfo()
car_02.GetInfo()
print(vars(car_02))
'''
print(car_01.brand, car_01.model, car_01.IsDamaged())
print(car_02.brand, car_02.model, car_02.IsDamaged())

print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK, car_01.isMechanicOK)
print(car_02.brand, car_02.model, car_02.isAirBagOK, car_02.isPaintingOK, car_02.isMechanicOK)
'''