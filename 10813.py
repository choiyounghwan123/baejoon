n,m = map(int, input().split())
changeList = []

for i in range(m):
    changeList.append(list(map(int, input().split())))


basket = [i for i in range(1,n+1)]
for c in changeList:
    basket[c[0]-1],basket[c[1]-1] = basket[c[1]-1],basket[c[0]-1]

for i in basket:
    print(i, end=" ")



