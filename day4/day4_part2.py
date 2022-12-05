file = open('/home/carsten/aoc/day4/input.txt', 'r')
Lines = file.readlines()

nonOverlappingCount = 0

for line in Lines:
    line = line.replace("\n", "")
    sections = line.replace(",", "-", 1).split("-")
    print(sections)

    if int(sections[2]) > int(sections[1]):
        # int(sections[0]) > int(sections[3]):
        nonOverlappingCount = nonOverlappingCount + 1
    if int(sections[0]) > int(sections[3]):
        nonOverlappingCount = nonOverlappingCount + 1


print(1000 - nonOverlappingCount)
