with open("./inputs/day2.txt") as f:
    mylist = f.read().splitlines()

import re

counts = {
    'red': 12,
    'green': 13,
    'blue': 14
}
sum = 0
for line in mylist:
    add = True
    line_split = line.split(': ')
    id = int(line_split[0].split(' ')[1])
    pulls = re.split('; |, ', line_split[1])
    for pull in pulls:
        p = pull.split(' ')
        num = int(p[0])
        if num > counts[p[1]]:
            add = False
    if add:
        sum += id

print(sum)

sum1 = 0

for line in mylist:
    line_split = line.split(': ')
    id = int(line_split[0].split(' ')[1])
    pulls = re.split('; |, ', line_split[1])
    t_count = {
        'red': 0,
        'green': 0,
        'blue': 0
        }
    for pull in pulls:
        p = pull.split(' ')
        t_count[p[1]] = max(t_count[p[1]], int(p[0]))
    add = 1
    for v in t_count.values():
        add *= v
    sum1 += add

print(sum1)