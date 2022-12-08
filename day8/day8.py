file = open('/home/carsten/aoc/day8/input.txt', 'r')
Lines = file.readlines()

matrix = []


def createForest():
    for i in range(len(Lines)):
        line = Lines[i].replace("\n", "")
        matrix.append(list(map(int, line)))


createForest()

height, width = len(matrix), len(matrix[0])
totalVisibleTrees = 0
totalVisibleTrees += 2 * (len(matrix[0]) + len(matrix) - 2)

for row in range(1, height - 1):
    currentRow = matrix[row]
    for col in range(1, width - 1):
        top = [matrix[i][col] for i in range(row - 1, -1, -1)]
        bottom = [matrix[i][col] for i in range(row + 1, height)]
        left = [currentRow[i] for i in range(col - 1, -1, -1)]
        right = [currentRow[i] for i in range(col + 1, width)]
        if currentRow[col] > max(top) or \
                currentRow[col] > max(bottom) or \
                currentRow[col] > max(right) or \
                currentRow[col] > max(left):
            totalVisibleTrees += 1
print(totalVisibleTrees)
