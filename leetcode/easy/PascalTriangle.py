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

print("res is %s" % generate(5))