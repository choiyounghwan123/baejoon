n,m = map(int, input().split())
arr2D = []
for i in range(m):
    arr2D.append(list(map(int,input().split())))

basket = [0 for i in range(n)]
for i in arr2D:
    for j in range(i[0]-1,i[1]):
        basket[j] = i[2]

for i in basket:
    print(i,end=" ")

