#assert - zalożenie stwierdzenie

import datetime
netto = 1230
brutto = 1000
# netto must be less or equal to brutto (assert zamiast tego komentarza)
assert netto <= brutto, "Netto cannot be greater than brutto"
#sprawdza poprawność załozenia i zwraca bład gdy się nie zgadza - kod się sam dokumentuje jak w assert dodamy komunikat błędu

orderDate = datetime.date(2022,11,13)
deliveryDate = datetime.date(2022,10,18)
# order date should be earlier than the delivery date
assert orderDate <= deliveryDate, "Order date should be earlier than the delivery date"

# jak się ustawi zmienną (to dla Windows): SET PYTHONOPTIMIZE=TRUE
# Wówczas są ignorowane polecenia ssert