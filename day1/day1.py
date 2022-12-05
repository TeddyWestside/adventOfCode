file1 = open('/home/carsten/aoc/day1/input.txt', 'r')
Lines = file1.readlines()

currentSum = 0
maxSum = 0
for line in Lines:
    if line.strip() == "":
        print(currentSum)
        if currentSum > maxSum:
            maxSum = currentSum
        currentSum = 0
    else:
        currentSum += int(line.strip())
print(maxSum)
