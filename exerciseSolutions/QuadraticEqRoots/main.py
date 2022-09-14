
def quadratic_eq_roots(a, b, c):
    discr = b**2 - 4.0 * a * c
    if discr > 0:
        r1 = (-b - discr**0.5) / 2.0 * a
        r2 = (-b + discr**0.5) / 2.0 * a
        print(f'Az egyenlet gyökei {r1} és {r2}.')
    elif discr == 0:
        r12 = -b / 2.0 * a
        print(f'Az egyenlet kettős gyöke {r12}.')
    else:
        print(f'Az egyenletnek nincs valós gyöke.')


if __name__ == '__main__':
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    quadratic_eq_roots(a, b, c)
