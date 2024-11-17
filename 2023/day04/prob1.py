import re


def worth(win, num) :
    w = False
    n = 0
    for m in num :
        if m in win :
            n += 1
            w = True
    if w :
        return 2**(n-1)
    return 0


def parse(line) :
    win = re.search(":.*\d+.*\|", line).group()
    win = re.findall("\d+", win)
    win = [int(n) for n in win]
    num = re.search("\|.*\d+.*", line).group()
    num = re.findall("\d+", num)
    num = [int(n) for n in num]
    return win, num


if __name__ == "__main__" :
    file = open("2023/day04/input.txt")
    lines = file.readlines()
    file.close()
    n = 0
    for line in lines :
        win, num = parse(line)
        n += worth(win, num)
    print(n)