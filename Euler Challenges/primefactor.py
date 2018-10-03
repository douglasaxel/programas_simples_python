n = 600851475143
factors = []
for factor in range(1, n + 1):
    if n % factor == 0:
        n = n / factor
        factors.append(factor)
        print(factors[-1])




# 13195|5
# 2639 |7
# 377  |13
# 29   |29
# 1    |
