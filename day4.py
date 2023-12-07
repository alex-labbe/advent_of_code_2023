with open("./inputs/day4.txt") as f:
    mylist = f.read().splitlines()
winning = []
my_nums = []

part_2 = []
sum = 0
for l in mylist:
    nums = l.split(' | ')
    w_char = nums[0].split(': ')[1].split(' ')
    w_nums = []
    for n in w_char:
        if n.isnumeric():
            w_nums.append(int(n))
    winning.append(w_nums)


    my_char = nums[1].split(' ')
    m_nums = []
    for n in my_char:
        if n.isnumeric():
            m_nums.append(int(n))
    my_nums.append(m_nums)

    num_matches = len([value for value in w_nums if value in m_nums])
    points = int(pow(2, num_matches-1))
    sum += points
    part_2.append([num_matches, 1])

for _ in range(len(part_2)):
    for i in range(part_2[_][0]):
        part_2[_+i+1][1] += part_2[_][1]

sum2 = 0
for _ in part_2:
    sum2 += _[1]
print(sum)
print(sum2)