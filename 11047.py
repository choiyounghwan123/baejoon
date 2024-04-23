n, target = map(int,input().split())
coins = []
ans = 0
for i in range(n):
    coins.append(int(input()))

for i in range(len(coins)-1,-1,-1):
    if target < coins[i]:
        continue

    ans += target // coins[i]
    target = target % coins[i]
print(ans)