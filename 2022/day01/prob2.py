import numpy as np


if __name__ == "__main__" :
    file = open("2022/day01/input.txt")
    lines = [line[:-1] for line in file.readlines()]
    file.close()
    cal = [0]
    i = len(lines) - 1
    while i >= 0 :
        if lines[i] == '' :
            cal.append(0)
        else :
            cal[-1] += int(lines[i])
        i -= 1
    maxes = cal[:3]
    for i in range(3, len(cal)) :
        if cal[i] > min(maxes) :
            maxes[np.argmin(maxes)] = cal[i]
    print(sum(maxes))