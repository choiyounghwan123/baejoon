students = [0 for i in range(1,31)]
for i in range(28):
    students[int(input())-1] = 1

for i in range(len(students)):
    if students[i] == 0:
        print(i+1)




