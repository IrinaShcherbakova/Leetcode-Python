def countAndSay(n):
   currentTerm = "1"
   i = 1
   while i < n:
       currentTerm = readTerm(currentTerm)
       i += 1
   return currentTerm


def readTerm(string):
    res = ""
    i = int(string[0])
    j = counter = 0
    while j < len(string):
        while j < len(string) and int(string[j]) == i:
            counter += 1
            j += 1
        res = res + str(counter) + str(i)
        counter = 0
        if j < len(string):
            i = int(string[j])
    return res


print("res is %s" % countAndSay(1))