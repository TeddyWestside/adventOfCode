file = open('/home/carsten/aoc/day4/input.txt', 'r')
Lines = file.readlines()

fullyContained = 0

for line in Lines:
    line = line.replace("\n", "")
    sections = line.replace(",", "-", 1).split("-")
    print(sections)

    if int(sections[2]) >= int(sections[0]) and int(sections[3]) <= int(sections[1]):
        fullyContained = fullyContained + 1
    if int(sections[0]) >= int(sections[2]) and int(sections[1]) <= int(sections[3]):
        fullyContained = fullyContained + 1
    if int(sections[2]) == int(sections[0]) and int(sections[3]) == int(sections[1]):
        fullyContained = fullyContained - 1

print(fullyContained)
