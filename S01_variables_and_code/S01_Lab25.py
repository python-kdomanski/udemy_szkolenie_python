projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for p, l in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(p, l))

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for p, l, d in zip(projects, leaders, dates):
    print('The leader of "{}" started {} is {}'.format(p, d, l))

for i, (p, l, d) in enumerate(zip(projects, leaders, dates)):
    print('{} - The leader of "{}" started {} is {}'.format(i + 1, p, d, l))