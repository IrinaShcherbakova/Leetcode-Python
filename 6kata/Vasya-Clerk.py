def tickets(people):
    counter25 = 0
    counter50 = 0
    for person in people:
        if person == 25:
            counter25 += 1
            continue
        if person == 50:
            if counter25 == 0:
                return "NO"
            else:
                counter25 -= 1
                counter50 += 1
                continue
        else:
            if counter50 > 0 and counter25 > 0:
                counter50 -= 1
                counter25 -= 1
                continue
            if counter25 < 3:
                return "NO"
            counter25 -= 3
    return "YES"

print("res is %s" % tickets([25, 25, 50]))
