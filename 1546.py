n = int(input())
scores = list(map(int, input().split()))

print(sum([i/max(scores) * 100for i in scores])/n)