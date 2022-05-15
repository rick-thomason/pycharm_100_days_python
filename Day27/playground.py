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
