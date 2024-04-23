str = input().lstrip().rstrip()
if len(str) == 0:
    print("0")
else:
    print(len(str.split(' ')))