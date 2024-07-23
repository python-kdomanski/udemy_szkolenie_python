brandOnSale = 'Opel'
class Car (object): #Dziedziczy z generycznej klasy objec - jest to tożsame z clacc Car():
#zmienne definiowane na poziomie klasy a nie instancji klasy'
    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        print('>> This is __init__ of parent class', self.__class__.__name__)
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale  #jak zaczyna się od __ to oznacza że jest to wewnętrzne/ukryte
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

class Truck(Car): #Truck dziedziczy z Car
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale, capacityKg):
        print('>> This is __init__ of child class', self.__class__.__name__)
        super().__init__(brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale) #super() - odwol anie się do instancji klasy rodzicielskiej (domyślnie super(Truck, self))
        #Car.__init__(self,brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale) - inna metoda wywoływania
        self.capacityKg = capacityKg

    def GetInfo(self):
        super().GetInfo()
        print("CapacityKG  -      {}".format(self.capacityKg))

truck_01 = Truck('Ford', 'Transit', True, False, True, False, 1600)
truck_02 = Truck('Renault', 'Trafic', True, True, True, True, 1200)

print('Calling properties:')
print(truck_01.brand, truck_01.capacityKg, truck_01.IsOnSale, truck_02.brand, truck_02.capacityKg, truck_02.IsOnSale)

truck_01.GetInfo()
truck_02.GetInfo()

