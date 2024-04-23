from collections import Counter

str1 = input().upper()
hash_map = Counter(str1)

m = max(hash_map.values())
count = 0
ms = ""
for k,i in hash_map.items():
    if m == i:
        count+=1
        ms = k
    if count == 2:
        break

if count > 1:
    print("?")
else:
    print(ms)

