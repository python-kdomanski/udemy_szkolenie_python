def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8
transformations = [double, square, div2, negative]

print('Starting transformations')
tmp_return_value = number
for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))

number = 125
transformations = [square, square, div2, double]

print('Starting transformations')
tmp_return_value = number
for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))