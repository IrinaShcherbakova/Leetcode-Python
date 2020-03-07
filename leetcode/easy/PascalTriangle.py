def generate(numRows):
    triangle = []
    if numRows == 0:
        return triangle
    triangle.append([1])
    currentRow = 1
    while currentRow < numRows:
        newRow = [1]
        numberOfCells = currentRow + 1
        i = 1
        while i < numberOfCells - 1:
            newRow.append(triangle[-1][i - 1] + triangle[-1][i])
            i += 1
        newRow.append(1)
        triangle.append(newRow)
        currentRow += 1
    return triangle


def getRow(rowIndex):
    previousRow = []
    for i in range(0, rowIndex+1):
        newRow = [None for _ in range(i+1)]
        newRow[0] = newRow[-1] = 1
        for j in range(1, i):
            newRow[j] = previousRow[j-1] + previousRow[j]
        previousRow = newRow
    return previousRow



print("res is %s" % getRow(0))