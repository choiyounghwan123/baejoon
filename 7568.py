import sys
data = []
for i in range(int(sys.stdin.readline())):
    data.append(tuple(map(int,sys.stdin.readline().split())))

for i in range(len(data)):
    count = 1
    for j in range(len(data)):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count+=1
    print(count,end=" ")