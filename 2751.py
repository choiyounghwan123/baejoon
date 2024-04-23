import sys
nums = []
for i in range(int(sys.stdin.readline())):
    nums.append(int(sys.stdin.readline()))
nums = list(dict.fromkeys(nums))

for num in sorted(nums):
    print(num)