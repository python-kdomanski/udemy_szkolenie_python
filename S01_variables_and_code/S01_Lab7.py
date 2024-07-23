"""
Oto deklaracja zmiennej days:
days = ['mon','tue','wed','thu','fri','sat','sun']
należy utworzyć zmienną workdays, która początkowo będzie zawierać te same elementy co days
następnie należy usunąć z workdays dni wolne
na koniec wyświetl days i workdays i upewnij się, że sobota i niedziela zniknęły tylko z listy workdays
"""

days = ['mon','tue','wed','thu','fri','sat','sun']
workdays=days.copy()
workdays.pop()
workdays.pop()
"""
workdays.remove('sat')
workdays.remove('sun')
"""
print('Lista days: ', days)
print('Lista workdays: ', workdays)