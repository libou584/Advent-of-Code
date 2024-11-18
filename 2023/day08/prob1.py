import re


def next(element, dico, inst) :
    if inst == "L" :
        return dico[element][0]
    else :
        return dico[element][1]


if __name__ == "__main__" :
    file = open("2023/day08/input.txt")
    lines = file.readlines()
    file.close()
    sequence = re.findall("\w", lines[0])
    dico = {}
    for i in range(2, len(lines)) :
        matches = re.findall("\w\w\w", lines[i])
        dico[matches[0]] = (matches[1], matches[2])
    n = 0
    element = "AAA"
    while element != "ZZZ" :
        element = next(element, dico, sequence[n%len(sequence)])
        n += 1
    print(n)