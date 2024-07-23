carBrand = 'Seat'
carModel = 'Ibiza'
carIsAirBagOK = True
carIsPaintingOK = True
carIsMechanicOK = True

def IsCarDamaged(carIsAirBagOK, carIsPaintingOK, carIsMechanicOK):
    return not(carIsAirBagOK and carIsPaintingOK and carIsMechanicOK)

print(IsCarDamaged(carIsAirBagOK, carIsPaintingOK, carIsMechanicOK))

car_01 = {
'carBrand' : 'Seat',
'carModel' : 'Ibiza',
'carIsAirBagOK' : True,
'carIsPaintingOK' : True,
'carIsMechanicOK' : True
}

print(IsCarDamaged(car_01['carIsAirBagOK'], car_01['carIsPaintingOK'], car_01['carIsMechanicOK']))


def IsCarDamaged2(aCar):
    return not(aCar['carIsAirBagOK'] and aCar['carIsPaintingOK'] and aCar['carIsMechanicOK'])

print(IsCarDamaged2(car_01))

car_02 = {
'carBrand' : 'Opel',
'carModel' : 'Corsa',
'carIsAirBagOK' : True,
'carIsPaintingOK' : False,
'carIsMechanicOK' : True
}

print(IsCarDamaged2(car_02))

cars = [car_01,car_02]

for c in cars:
    print("{} {} damaged = {}".format(c['carBrand'],c['carModel'], IsCarDamaged2(c)))