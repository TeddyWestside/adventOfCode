from collections import Counter

file = open('/home/carsten/aoc/day6/input.txt', 'r')
line = file.readlines()[0]

for i in range(len(line)):
    sequence = line[i:i + 14]
    charCounter = Counter(sequence)
    if charCounter.keys().__len__() == 14:
        print(i + 14)
        break
