a, b = 0, 1
fib = 0
while a < 4000000:
    a, b = a + b, a
    print(a)
    if a % 2 == 0:
        fib += a
print(f'soma dos n pares: {fib}')
