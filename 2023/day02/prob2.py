import re


def power(line) :
    red, green, blue = 0, 0, 0
    matches = re.findall("\d+\s\w+", line)
    for match in matches :
        n = int(re.search("\d{1,2}", match).group())
        color = re.search("\w{3,5}", match).group()
        if color == "red" :
            red = max(red, n)
        elif color == "green" :
            green = max(green, n)
        else :
            blue = max(blue, n)
    return red*green*blue


if __name__ == "__main__" :
    file = open("2023/day02/input.txt")
    lines = file.readlines()
    file.close()
    # for i in range(len(lines)) :
    #     print(is_possible(lines[i]))
    n = 0
    for line in lines :
        n += power(line)
    print(n)