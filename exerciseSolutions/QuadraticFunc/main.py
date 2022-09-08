def quadratic(x):
    a = 10
    b = 9
    c = 8
    y = a * x ** 2 + b * x + c
    print(f'F(x) = {y}')


if __name__ == '__main__':
    x = float(input('Add meg az x értékét: '))
    quadratic(x)