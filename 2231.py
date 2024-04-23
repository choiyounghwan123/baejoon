num = int(input())

check = 1

for i in range(1,num+1):
    digits = sum([int(digit) for digit in str(i)])
    if i + digits == num:
        print(i)
        check = 0
        break

if check:
    print("0")