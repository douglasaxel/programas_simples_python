def fibonachi(n):
    a, b = 0, 1
    while b < n:
        print(a)
        a, b = b, a + b

fibonachi(1000)
