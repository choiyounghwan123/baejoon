a = int(input())
b = list(input())


print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
b = int("".join(b))
print(a*b)
