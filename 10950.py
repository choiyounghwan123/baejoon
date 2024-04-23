t = int(input())
ans = []
for i in range(t):
    a = map(int, input().split())
    ans.append(sum(a))

for i in ans:
    print(i)