n = int(input())

test_cases = []

for i in range(n):
    test_cases.append(input())

count = 1
score = 0
for test_case in test_cases:
    for j in test_case:
        if j == "O":
            score +=count
            count+=1
        else:
            count = 1
    print(score)
    score = 0
    count = 1