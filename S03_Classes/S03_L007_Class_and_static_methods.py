#Metody powiązanie z instacją jako 1 argument przyjmuje: self
#Metody powiązanie z klasą jako 1 argument przyjmuje: cls
#Metod statyczna nie ma zwiazkuz klasą - nie przyjmuje ani self ani cls

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

    @classmethod #dekorator dla metod pracujących na poziomie klasy
    def ReadFromText(cls,aText):
        aNewCar = cls(*aText.split(':')) #* przed aText - zamiast listy () zostaną przekazane odrębne wartości
        return aNewCar

    @staticmethod #dekorator dla metod statycznych - tematycznie łączy się z klasą Car a le nie zależy od klasy ani od instancji klasy
    def Convert_KM_KW(KM):
        return KM * 0.735

    @staticmethod #dekorator dla metod statycznych
    def Convert_KW_KM(KW):
        return KW * 1.36

lineOfText='Renault:Megane:True:True:False:False'
car_03 = Car.ReadFromText(lineOfText)

car_03.GetInfo()

print('convert 120 KM to KW',Car.Convert_KM_KW(120))
print('convert 90 KW to KM',Car.Convert_KW_KM(90))

car_01 = Car('Seta', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

'''
print("Status of cars", car_01.__GetIsOnSale(), car_02.__GetIsOnSale()) #to się wywali
print("Status of cars", car_01._Car__GetIsOnSale(), car_02._Car__GetIsOnSale()) #to zadziała
car_01.SetIsOnSale(True)
car_02.SetIsOnSale(False)
print("Status of cars", car_01.GetIsOnSale(), car_02.GetIsOnSale())

car_01.IsOnSale = True
car_02.IsOnSale = True
car_01.GetInfo()
car_02.GetInfo()
print("Status of cars", car_01.IsOnSale, car_02.IsOnSale)
'''
'''
print(car_01.brand, car_01.model, car_01.IsDamaged())
print(car_02.brand, car_02.model, car_02.IsDamaged())

print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK, car_01.isMechanicOK)
print(car_02.brand, car_02.model, car_02.isAirBagOK, car_02.isPaintingOK, car_02.isMechanicOK)
'''