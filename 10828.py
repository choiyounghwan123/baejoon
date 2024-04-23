class Stack:
    def __init__(self):
        self.data = []

n = int(input())
stack = []
for i in range(n):
    order, = map(str, input())

    if