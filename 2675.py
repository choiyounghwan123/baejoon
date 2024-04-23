n = int(input())

for i in range(n):
    num, s = map(str, input().split())
    for j in s:
        print(j * int(num),end="")
    print("")