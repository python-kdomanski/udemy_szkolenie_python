cake_01 = {'taste': 'vanilia',
           'glaze': 'chocolade',
           'text': 'Happy Brithday',
           'weight': 0.7}

cake_02 = {'taste': 'tee',
           'glaze': 'lemon',
           'text': 'Happy Python Coding',
           'weight': 1.3}


def show_cake_info(a_cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        a_cake['taste'], a_cake['glaze'], a_cake['text'], a_cake['weight']))


cakes = [cake_01, cake_02]

for a_cake in cakes:
    show_cake_info(a_cake)

