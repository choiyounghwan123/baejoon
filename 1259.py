while True:
    num = input()

    if num == "0":
        break

    check = num[::-1] == num

    if check:
        print("yes")
    else:
        print("no")
