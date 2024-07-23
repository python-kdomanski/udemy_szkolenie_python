import csv
import types

#Metody powiązanie z instacją jako 1 argument przyjmuje: self
#Metody powiązanie z klasą jako 1 argument przyjmuje: cls
#Metod statyczna nie ma zwiazkuz klasą - nie przyjmuje ani self ani cls

def exportToFile_Static(path, header, data):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    print('>>> This is function exportToFile - statis method')

def exportToFile_Class(cls, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','IsOnSale'])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    print('>>> This is function exportToFile - class method')

def exportToFile_Instance(self, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','IsOnSale'])
        writer.writerow([self.brand, self.model, self.IsOnSale])
    print('>>> This is function exportToFile - instance method')

brandOnSale = 'Opel'
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

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsonSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale=newIsonSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsonSaleStatus,self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'if set to true, the car is available in sale/promo')
                        # nazwa funkcjo do pobrania, nazwa funkcj do zmiany, nazwa funkcji do usunjięcia, opis/dokumentacja


car_01 = Car('Seta', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

print('Static----------'*10)
Car.ExportToFile_Static = exportToFile_Static
#exportToFile_Static(r'd:\Projekty\PyCharm\pythonCourse\S03_Classes\exprt_static_csv',['Brand','Model','IsOnSale'],[car_01.brand, car_01.model,car_01.IsOnSale])
Car.ExportToFile_Static(r'd:\Projekty\PyCharm\pythonCourse\S03_Classes\exprt_static_csv',['Brand','Model','IsOnSale'],[car_01.brand, car_01.model,car_01.IsOnSale])
print(dir(Car))

print('Class----------'*10)
Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car) #1 pa = nazwa zewnętrznej funkcji, 2 par - nazwa klasy
Car.ExportToFile_Class(path=r'd:\Projekty\PyCharm\pythonCourse\S03_Classes\exprt_class_csv')
print(dir(Car))

print('Instance class----------'*10)
car_01.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01) #1 pa = nazwa zewnętrznej funkcji, 2 par - nazwa klasy
car_01.ExportToFile_Instance(path=r'd:\Projekty\PyCharm\pythonCourse\S03_Classes\exprt_instance_csv')
print(dir(car_01))

print('-'*50)
#metoda istnieje gdy jest atrybut o nazwie klasy i jest on callable
if hasattr(car_01, 'ExportToFile_Static') and callable(car_01.ExportToFile_Static):
    print("The object has method ExportToFile_Static")

if hasattr(car_01, 'ExportToFile_Class') and callable(car_01.ExportToFile_Class):
    print("The object has method ExportToFile_Class")

if hasattr(car_01, 'ExportToFile_Instance') and callable(car_01.ExportToFile_Instance):
    print("The object has method ExportToFile_Instance")

if hasattr(car_01, 'IsOnSale') and callable(car_01.IsOnSale):
    print("The object has method IsOnSale")
else:
    print('no such metod')
