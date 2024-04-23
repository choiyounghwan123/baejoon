n = int(input())

for i in range(n):
    k = int(input())
    n = int(input())

    arr1 = [i for i in range(1,n+1)]
    for j in range(k):
        for q in range(1,n):
            arr1[q] = arr1[q-1] + arr1[q]
    print(arr1[-1])