file = open('/home/carsten/aoc/day3/input.txt', 'r')
Lines = file.readlines()

weights = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
weightsSum = 0

for line in Lines:
    lineCharArray = list(line)
    lineCharArray = lineCharArray[:-1]
    print(lineCharArray)
    halfArrayLength = len(lineCharArray) // 2
    firstHalfArray = lineCharArray[:halfArrayLength]
    secondHalfArray = lineCharArray[halfArrayLength:]
    # totalScore += scoresPart1.get(trimmedLine)
    result = list(filter(lambda x: x in firstHalfArray, secondHalfArray))
    weightsSum += weights.index(result[0])+1
print(weightsSum)

