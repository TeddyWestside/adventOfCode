file = open('/home/carsten/aoc/day5/input.txt', 'r')
Lines = file.readlines()


def createStackArray():
    stacks = [["D", "T", "W", "F", "J", "S", "H", "N"], ["H", "R", "P", "Q", "T", "N", "B", "G"], ["L", "Q", "V"],
              ["N", "B", "S", "W", "R", "Q"], ["N", "D", "F", "T", "V", "M", "B"], ["M", "D", "B", "V", "H", "T", "R"],
              ["D", "B", "Q", "J"], ["D", "N", "J", "V", "R", "Z", "H", "Q"], ["B", "N", "H", "M", "S"]]
    return stacks


stackArray = createStackArray()

for lineIndex in range(len(Lines)):
    line = Lines[lineIndex].replace("\n", "")
    if line.strip().startswith("m"):
        splittedLine = line.split(" ")

        amount = int(splittedLine[1])
        source = int(splittedLine[3])
        target = int(splittedLine[5])

        toBeAdded = []
        for i in range(amount):
            toBeAdded.append(stackArray[source - 1].pop())
        toBeAdded.reverse()  # For part 2
        for item in toBeAdded:
            stackArray[target - 1].append(item)

goal = ""
for stack in stackArray:
    goal = goal + stack.pop()

print(goal)
