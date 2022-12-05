file1 = open('/home/carsten/aoc/day2/input.txt', 'r')
Lines = file1.readlines()

# scoresPart1 = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ": 6}
scoresPart2 = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}
totalScore = 0
for line in Lines:
    trimmedLine = line.strip().replace(" ", "", 1)
    # totalScore += scoresPart1.get(trimmedLine)
    totalScore += scoresPart2.get(trimmedLine)
print(totalScore)
