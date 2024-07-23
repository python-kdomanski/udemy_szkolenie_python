brandOnSale = 'Opel'

class Car (): #Dziedziczy z generycznej klasy objec - jest to tożsame z clacc Car():
    """
    Car - class operating on cars available in the delar
    """
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        """
        init - argument accepted:
        brand - the brand of the class
        :param model:
        :param isAirBagOK:
        :param isPaintingOK:
        :param isMechanicOK:
        :param isOnSale:
        """
        print('>> This is __init__ of parent class', self.__class__.__name__)
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale  # jak zaczyna się od __ to oznacza że jest to wewnętrzme/ukryte

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag  - ok      {}".format(self.isAirBagOK))
        print("Painting - ok      {}".format(self.isPaintingOK))
        print("Mechanic - ok      {}".format(self.isMechanicOK))
        print("Is on sale         {}".format(self.__isOnSale))
        print('-------------------------------')

    @property  # oznaczanie, że funkcja jest właściwością
    def IsOnSale(self):
        """IsOnSame - the car is on extra promotion that is limited in time (only selected cars may be "On sale")"""
        return self.__isOnSale

    @IsOnSale.setter  # dekorator - nazwa taka jak nazwa funkcji+setter, przed musi być właściwośc do pobrania @property
    def IsOnSale(self, newIsonSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsonSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsonSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None

    @property
    def CarTitle(self):
        return "Brand: {}, Model: {}".format(self.brand, self.model).title()


car_01 = Car('Seta', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

print(car_01.IsOnSale)
car_01.IsOnSale = True
del car_01.IsOnSale  # da sie usunać gdy jest metoda do delete

print(car_01.IsOnSale)

print(car_01.CarTitle)

help(Car)
help(Car.IsOnSale) #CTRL+Q podpowiedz jak się wywołuje metodę/...