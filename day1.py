elves = []
temp = []
with open('input.txt', 'r') as f:
    for line in f:
        if line != '\n':
            temp.append(int(line))
        else:
            elves.append(temp)
            temp = []

print(elves)

max_calory = 0
index = 0
for i, elf in enumerate(elves):
    temp = sum(elf)
    if temp > max_calory:
        max_calory = temp
        index = i

print(max_calory)
