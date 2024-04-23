import sys

n = int(input())

nums = [0 for i in range(0,10000)]

for i in range(n):
    nums[int(sys.stdin.readline())-1] += 1

for i in range(len(nums)):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i+1)