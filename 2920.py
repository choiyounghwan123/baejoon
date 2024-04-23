nums = list(map(int,input().split()))

check1 = True
for i in range(1,8):
    if nums[i] != nums[i-1] +1:
        check1 = False
        break
check2 = True
if check1:
    print("ascending")
else:
    for i in range(1, 8):
        if nums[i] != nums[i - 1] - 1:
            check2 = False
            break
    if check2:
        print("descending")
    else:
        print("mixed")

