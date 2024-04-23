import math

while True:
    sides = list(map(int,input().split()))

    if all(side == 0 for side in sides):
        break

    sides.sort()

    if math.sqrt(sides[0] ** 2 + sides[1] ** 2) == math.sqrt(sides[2] ** 2):
        print("right")
    else:
        print("wrong")