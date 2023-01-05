def test(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for n in range(2, 1001):
    if test(n):
        print(n)
