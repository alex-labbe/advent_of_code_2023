with open("./inputs/day1.txt") as f:
    mylist = f.read().splitlines()

sum = 0
for line in mylist:
    l = len(line)-1
    i = 0
    while line[i].isalpha():
        i += 1
    while line[l].isalpha():
        l -= 1
    sum += int(line[i]+line[l])

print(sum)

words = {
    "one": 'o1e',
    "two": 't2e',
    "three": 't3e',
    "four": 'f4r',
    "five": 'f5e',
    "six": 's6x',
    "seven": 's7n',
    "eight": 'e8t',
    "nine": 'n9e'
}


sum2 = 0

for line in mylist:
    curr = line
    for k, v in words.items():
        curr = curr.replace(k, v)
    
    l = len(curr)-1
    i = 0
    while curr[i].isalpha():
        i += 1
    while curr[l].isalpha():
        l -= 1
    add = int(curr[i]+curr[l])
    sum2 += add

print(sum2)