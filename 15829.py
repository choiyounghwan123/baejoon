l = int(input())

str1 = input()
result = 0
for i in range(len(str1)):
    result+= ((ord(str1[i]) - 96) * (31) ** i)
print(result% 1234567891)