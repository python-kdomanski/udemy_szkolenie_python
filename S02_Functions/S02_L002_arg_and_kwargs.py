def BuyMe(prefix='Please buy me', what='something nice', *args, **kwargs):
    print(prefix,what)
    print(args)
    print(kwargs)
    # *nazwa_zmiennej - lista dodatkowych argumentów (tuplet)
    # **nazwa - lista dodatkowych argumentów poprzedzonych nazwą (słownik), kw-keyy word args-argument

BuyMe('Please buy me', 'a new car', 'a dog', 'a cat', shop='market', color='yelow')
products = ['milk', 'bread', 'flakes']
parameters = {'proce':'low', 'time':'now'}
BuyMe('Buy me', 'newspaper', products, parameters)
BuyMe('Buy me', 'newspaper', *products, **parameters)