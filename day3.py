with open("./inputs/day3.txt") as f:
    mylist = f.read().splitlines()

l = len(mylist[1])
h = len(mylist)

def gen_points(x, y):
    curr = complex(x, y)
    points = []

    points.append(curr+1)
    points.append(curr-1)
    points.append(curr+1j)
    points.append(curr-1j)
    points.append(curr + 1 + 1j)
    points.append(curr - 1 + 1j)
    points.append(curr + 1 - 1j)
    points.append(curr - 1 - 1j)

    f = []

    for p in points:
        if p.real >= 0 and p.real < h and p.imag >= 0 and p.imag < l:
            f.append(p)

    return f


def get_num(x, y):
    line = mylist[x]
    left, right = y, y+1
    while line[left].isnumeric() and left >= 0:
        left -= 1
    left += 1
    while right < l and line[right].isnumeric():
        right += 1
    num = int(line[left:right])
    num_len = right - left
    replace = '.'*num_len
    #t = line[right:l]
    mylist[x] = line[0:left] + replace + line[right:l]
    return num

## real is updown, imag is leftright


sum = 0
for x in range(h):
    for y in range(l):
        c = mylist[x][y]
        if c in '/=@#$%&*-+':
            p = gen_points(x, y)
            for points in p:
                if mylist[int(points.real)][int(points.imag)].isnumeric():
                    sum += get_num(int(points.real), int(points.imag))


sum2 = 0
with open("./inputs/day3.txt") as f:
    mylist = f.read().splitlines()

for x in range(h):
    for y in range(l):
        c = mylist[x][y]
        if c in '*':
            nums = []
            p = gen_points(x, y)
            for points in p:
                if mylist[int(points.real)][int(points.imag)].isnumeric():
                    nums.append(get_num(int(points.real), int(points.imag)))
            if len(nums) == 2:
                sum2 += nums[0] * nums[1]



print(sum)
print(sum2)