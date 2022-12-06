from collections import Counter

file = open('/home/carsten/aoc/day6/input.txt', 'r')
line = file.readlines()[0]

for i in range(len(line)):
    sequence = line[i:i + 4]

    charCounter = Counter(sequence)
    if charCounter.keys().__len__() == 4:
        print(i+4)
        break

    # print(line[i:i+4])
