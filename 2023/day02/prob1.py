import re


def is_possible(line) :
    matches = re.findall("\d+\s\w+", line)
    for match in matches :
        n = int(re.search("\d{1,2}", match).group())
        color = re.search("\w{3,5}", match).group()
        if (color == "red" and n > 12) or (color == "green" and n > 13) or (color == "blue" and n > 14) :
            return False
    return True


if __name__ == "__main__" :
    file = open("2023/day02/input.txt")
    lines = file.readlines()
    file.close()
    # for i in range(len(lines)) :
    #     print(is_possible(lines[i]))
    n = 0
    for i in range(len(lines)) :
        if is_possible(lines[i]) :
            n += i+1
    print(n)