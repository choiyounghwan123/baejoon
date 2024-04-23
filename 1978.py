n = int(input())

prime = [True] * 1001
prime[0] = False
prime[1] = False
p = 2
while p*p < 1000:
    if prime[p] == True:
        for i in range(p*p,1001,p):
            prime[i] = False
    p+=1


answer = 0

numbers = list(map(int,input().split()))
for number in numbers:
    if prime[number] == True:
        answer+=1

print(answer)
