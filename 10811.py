n,m = map(int, input().split())
r = []
basket = [i for i in range(1,n+1)]
for i in range(m):
    r.append(list(map(int, input().split())))
for c in r:
    basket = basket[:c[0]-1] + list(reversed(basket[c[0]-1:c[1]])) + basket[c[1]:]

for b in basket:
    print(b,end=" ")