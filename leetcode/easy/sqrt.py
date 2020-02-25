
def mySqrt(x):
    for i in range(0, x//2 + 2):
        squaredI = i*i
        if squaredI < x:
            continue
        if squaredI == x:
            return i
        else:
            return i - 1
    return 1


print("res is %s" % mySqrt(5))