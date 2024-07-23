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
    print("The % ratio for {} is {}".format(myClient,clients[myClient]))
except Exception as e: #gdy błąd
    print("Błędny klient...\nDetails:\n{}".format(e))
else: #wykonuje się gdy nie ma błędu
    print("The cost form {} id {}".format(myClient,clients[myClient] * totalCost))
finally: #wykonuje się zawsze
    print("--- koniec kalkulacji ---")
