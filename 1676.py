import math

n = math.factorial(int(input()))

n_spl = [int(num) for num in str(n)]


for i in range(len(n_spl)):
    if 0 != n_spl[(-i)-1]:
        print(i)
        break