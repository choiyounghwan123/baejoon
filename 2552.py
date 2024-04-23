a,b = map(int, input().split())
c = int(input())

if b + c >= 60:
    time = (b+c) // 60
    b = (b+c) % 60
    if a +time > 23:
        a = ((a+time) % 24)
    else:
        a+=time
else:
    b += c

print(a, b)