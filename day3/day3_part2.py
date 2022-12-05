file = open('/home/carsten/aoc/day3/input.txt', 'r')
Lines = file.readlines()

weights = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
weightsSum = 0

firstElf = ""
secondElf = ""
thirdElf = ""
index = 0

for line in Lines:
    index = index + 1
    lineCharArray = list(line)
    lineCharArray = lineCharArray[:-1]
    if index == 1:
        firstElf = lineCharArray
    if index == 2:
        secondElf = lineCharArray
    if index == 3:
        thirdElf = lineCharArray

        resultFirstSecond = list(filter(lambda x: x in firstElf, secondElf))
        resultAll = list(filter(lambda x: x in resultFirstSecond, thirdElf))
        print(resultAll)
        weightsSum += weights.index(resultAll[0])+1
        index = 0
print(weightsSum)

