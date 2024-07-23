def BuyMe(prefix='Please buy me', what='something nice'):
    print(prefix,what)
#Parametry domyśle albo dla wszystkich albo dla żadnego, gdy wprowadzimy jakiś domyślny to wszystkie późmieniejsze parametry muszą też mieć domyślnych

BuyMe('Please buy me', 'a new car') #Przekazywanie parametrów przez pozycję
BuyMe(prefix='Please buy me', what='a new car') #Przekaywanie parametrów przez nazwę
BuyMe(what='a new car', prefix='Please buy me')

BuyMe('Please')

BuyMe(prefix='Please buy me')
BuyMe(what='something sweet')
BuyMe()