import re


def match_num(win, num) :
    n = 0
    for m in num :
        if m in win :
            n += 1
    return n


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
    cards = [1 for i in range(len(lines))]
    for i in range(len(lines)) :
        win, num = parse(lines[i])
        n = match_num(win, num)
        for j in range(i+1, i+n+1) :
            cards[j] += cards[i]
    print(sum(cards))