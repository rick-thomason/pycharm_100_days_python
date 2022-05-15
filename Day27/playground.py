def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(2, 6, 8))


def calculate(num, **kwargs):
    num += kwargs['add']
    num *= kwargs['multiply']
    return num


print(calculate(5, add=3, multiply=10))


class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')


my_car = Car(model='Camry')
print(my_car.make)
