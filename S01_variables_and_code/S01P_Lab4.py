"""
    W pierwszym przypadku zainicjuj zmienne a, b, c wartością 10. W tym celu wykonaj tylko
    jedną instrukcję.
    Wyświetl wartości zmiennych oraz ich identyfikatory
    Następnie zmień wartość zmiennej a np. na 20
    Ponownie wyświetl wartości zmiennych i ich identyfikatory
(identyfikator zmiennej a powinien się zmienić)
"""
a=b=c=10
print(a, id(a))
print(b, id(b))
print(c, id(c))
a=20
print(a, id(a))
print(b, id(b))
print(c, id(c))

print('---------------------------------------')

"""
Teraz wykonaj jeszcze raz te same czynności, co poprzednio ale z delikatną różnicą:
    zmienne a, b i c mają mieć przypisaną wartość w postaci listy, np. [1,2,3]
    modyfikacja zmiennej a ma polegać na dodaniu do listy a nowego elementu, np. liczby 4
(identyfikator zmiennej a powinien być teraz taki sam jak b i c, dodatkowo zmieni się jednocześnie lista w zmiennych b i c)
"""

a=b=c=[1,2,3]
print(a, id(a))
print(b, id(b))
print(c, id(c))
a.append(4)
print(a, id(a))
print(b, id(b))
print(c, id(c))

print('---------------------------------------')

"""
Uwaga - w tym zadaniu można się spodziewać, że w różnych wersjach Pytona uzyskamy różne wyniki, ale spróbujmy...
    Do zmiennej x przypisz wartość 10
    Do zmiennej y przypisz wartość 10 (użyj przypisań w dwóch osobnych liniach!)
    Wyświetl id tych zmiennych
(chociaż mamy do czynienia z dwoma niezależnymi zmiennymi, to optymalizator pythona nadał im ten sam id)
"""

x=10
y=10
print(x, id(x))
print(y, id(y))

print('---------------------------------------')

"""
Do zmiennej y przypisz wartość y plus 1 minus 1.
Sprawdź identyfikatory zmiennych x i y
(identyfikatory nadal powinny być takie same, tzn. optymalizator poradził sobie z prostym działaniem + 1 - 1)
"""

y=y+1
y=y-1
print(x, id(x))
print(y, id(y))

print('---------------------------------------')

"""
Powtórz operację dodawania i odejmowania od y, ale tym razem dodaj i odejmij wartość 1234567890
Sprawdź identyfikatory zmiennych x i y
(identyfikatory powinny być różne, tzn. optymalizator nie rozpoznał, że zmienne mają nadal te same wartości)
"""

y=y+1234567890
y=y-1234567890
print(x, id(x))
print(y, id(y))