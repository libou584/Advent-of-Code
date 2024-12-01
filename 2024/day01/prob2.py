import re


def sort(l) :
    if len(l) == 0 or len(l) == 1 :
        return l
    p = l[0]
    l1, l2, l3 = [], [], []
    for n in l :
        if n < p :
            l1.append(n)
        elif n > p :
            l3.append(n)
        else :
            l2.append(n)
    return sort(l1) + l2 + sort(l3)


def in_right(num, right) :
    m = 0
    for n in right :
        if n == num :
            m += 1
        elif n > num :
            break
    return m



if __name__ == "__main__" :
    file = open("2024/day01/input.txt")
    lines = file.readlines()
    file.close()
    left = []
    right = []
    for line in lines :
        matches = re.findall("\d+", line)
        left.append(int(matches[0]))
        right.append(int(matches[1]))
    left = sort(left)
    right = sort(right)
    tot = 0
    i = 0
    while i < len(left) :
        num = left[i]
        n = 0
        while i < len(left) and left[i] == num :
            n += 1
            i += 1
        m = in_right(num, right)
        tot += n*m*num
    print(tot)