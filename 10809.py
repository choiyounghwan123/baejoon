s = list(input())
alpahbets = [-1 for i in range(26)]

for i in range(len(s)):
    if alpahbets[ord(s[i])%97] == -1:
        alpahbets[ord(s[i])%97] = i

for i in alpahbets:
    print(i,end=" ")