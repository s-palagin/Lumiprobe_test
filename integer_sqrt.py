def int_sqrt(n):
    if type(n) is int and n >= 0:
        sqrt = int(n ** 0.5)
        return sqrt if sqrt ** 2 == n else None
    raise ValueError(f'N must be positive integer number, not {n}')
    
if __name__ == '__main__':
    assert int_sqrt(4) == 2, 'sqrt(4) == 2'
    assert int_sqrt(8) is None, 'sqrt(8) - not integer'
    try:
        int_sqrt(-1)
    except ValueError:
        print('Test - ok!')
