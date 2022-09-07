# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def quadratic(x):
    a = 10
    b = 9
    c = 8
    y = a * x**2 + b * x + c
    print(f'F(x) = {y}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = float(input('Add meg az x értékét: '))
    quadratic(x)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
