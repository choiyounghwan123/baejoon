n = int(input())
words = []
for i in range(n):
    words.append(input())

words = list(dict.fromkeys(words))
words.sort(key= lambda word: (len(word),word))

for word in words:
    print(word)

