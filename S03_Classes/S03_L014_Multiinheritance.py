class Car ():

    def __init__(self, brand, model, isOnSale):
        print('>> Class Car - __init__ starting')
        self.brand = brand
        self.model = model
        self.isOnSale = isOnSale
        self.name = "{} {}".format(brand, model)
        print('>> Class Car - __init__ finishing')

    def GetInfo(self):
        print('>> Class Car - GetInfo - starting')
        super().GetInfo() #tak by wywołała się metoda we wszystkich klasach dziedziczonych (zaremuj i sprawdx)
        print("{} {}".format(self.brand, self.model).upper())
        print("Is on sale         {}".format(self.isOnSale))
        print('>> Class Car - GetInfo - stopping')

class Specialist:

    def __init__(self, firstname, lastname, brand):
        print('>> Class Specialist - __init__ starting')
        self.firstname = firstname
        self.lastname = lastname
        self.name = "{} {}".format(firstname, lastname)
        self.brand = brand
        print('>> Class Specialist - __init__ finishing')

    def GetInfo(self):
        print('>> Class Specialist - GetInfo - starting')
        print("{} {} - ({})".format(self.firstname, self.lastname, self.brand))
        print('>> Class Specialist - GetInfo - stopping')

class CarSpecialist(Car, Specialist):

    def __init__(self, brand, model, isOnSale,firstname, lastname):
        print('>> Class CarSpecialist - __init__ starting')
        Car.__init__(self, brand, model, isOnSale)
        Specialist.__init__(self, firstname, lastname, brand.upper())
        print('>> Class CarSpecialist - __init__ finishing')


    def GetInfo(self):
        print('>> Class CarSpecialist - GetInfo - starting')
        super().GetInfo()
        print('>> Class CarSpecialist - GetInfo - stopping')

tom = CarSpecialist('Toyota','Corolla', True, 'Tom', 'Smith')
print(vars(tom))
tom.GetInfo()

#Method Resolution Order
print(CarSpecialist.__mro__)