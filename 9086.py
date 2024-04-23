n = int(input())
strList = []
for i in range(n):
    strList.append(input())

for s in strList:
    if len(s) == 0:
        print(s*2)
    else:
        print(s[0]+s[-1])