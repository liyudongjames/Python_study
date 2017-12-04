n = 0
while n < 50:
    for x in range(0, 80):
        count = 558 - 8 * x
        y = count / 9
        if(y.is_integer()):
            print(y, x)
        n = n + 1
