num = int(input())

i = 1
pre = 1
for i in range(0,num):
    if (6 * i)+pre >= num:
        print(i+1)
        break
    else:
        pre += 6*i