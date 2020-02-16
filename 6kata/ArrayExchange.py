def exchange_with(a, b):
    reversedA = []
    for i in a[::-1]:
        reversedA.append(i)
    a.clear()
    for i in b[::-1]:
        a.append(i)
    b.clear()
    for i in reversedA:
        b.append(i)
    return



a = ["1", "2", "3", "4", "5", "6", "7"]
b = ["a", "b", "c"]
exchange_with(a, b)
print(a)
print(b)
