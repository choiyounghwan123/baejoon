def upper(x):
    if x - int(x) > 0:
        return int(x)+1
    return int(x)


t = int(input())
hotels = []

for i in range(t):
    hotels.append(list(map(int, input().split())))

for hotel in hotels:
    floor1 = hotel[2] % hotel[0]

    if floor1 == 0:
        floor1 = hotel[0]

    room = upper((hotel[2] / hotel[0]))
    if len(str(room)) == 1:
        print(str(floor1) + "0" + str(room))
    else:
        print(str(floor1) + str(room))


