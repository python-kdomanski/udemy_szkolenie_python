class Cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')

bakery_offer = []
bakery_offer.append(cake01)
bakery_offer.append(cake02)
bakery_offer.append(cake03)

print("Today in our offer:")
for c in bakery_offer:
    print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(
        c.name, c.kind, c.taste, c.additives, c.filling))