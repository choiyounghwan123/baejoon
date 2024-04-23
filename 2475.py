num = map(str, input().split())
t = 0

for n in num:
    t+=int(n) ** 2

print(t%10)