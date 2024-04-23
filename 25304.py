total_price = int(input())
n = int(input())

for i in range(n):
    price, num = map(int, input().split())

    total_price -= price * num

if total_price == 0:
    print("Yes")
else:
    print("No")