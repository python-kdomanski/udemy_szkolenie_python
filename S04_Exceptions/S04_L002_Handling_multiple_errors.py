clients = {
    "INFO": 0.5,
    "DATA": 0.2,
    "SOFT": 0.2,
    "INTER": 0.1,
    "OMEGA": 0.0
}

myClient = input("Enter client name:")
totalCost = 7200

try:
    ratio = float(input("Enter new ratio: "))
    print("The % ratio for {} is {}, a new one is {}".format(myClient,clients[myClient], ratio))
    print("The cost form {} id {}".format(myClient, ratio * totalCost))
    print("The new ratio / to old ratio{}".format(clients[myClient]/ratio))
except KeyError as e:
    print("Klienta {} nie ma na liście klientów {} \n Details:\n {}".format(myClient,[c for c in clients.keys()],e))
except ValueError as e:
    print("Błędna wartość - to musi być liczba\nDetail\n{}".format(e))
except ZeroDivisionError as e:
    print("Ratio nie moze być 0\nDetail:\n".format(e))
except Exception as e: #gdy błąd
    print("Błąd...\nDetails:\n{}".format(e))
#except (ValueError, ZeroDivisionError) as e: #łączenie błędów
