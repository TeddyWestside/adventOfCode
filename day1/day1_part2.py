file1 = open('/home/carsten/aoc/day1/input.txt', 'r')
Lines = file1.readlines()

currentSum = 0
sumArray = []
for line in Lines:
    if line.strip() == "":
        print(currentSum)
        sumArray.append(currentSum)
        currentSum = 0
    else:
        currentSum += int(line.strip())

sortedArray = sorted(sumArray)
print(sortedArray[sortedArray.__len__()-1])

print(sortedArray[sortedArray.__len__()-3] +
      sortedArray[sortedArray.__len__()-2] +
      sortedArray[sortedArray.__len__()-1])
