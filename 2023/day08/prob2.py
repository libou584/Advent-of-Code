import re
import numpy as np


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
    elements = [element for element in dico.keys() if element[2] == "A"]
    cycles = [0 for i in range(len(elements))]
    for i in range(len(cycles)) :
        element = elements[i]
        while element[2] != "Z" :
            element = next(element, dico, sequence[cycles[i]%len(sequence)])
            cycles[i] += 1
    print(np.lcm.reduce(cycles))