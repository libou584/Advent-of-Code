def value(pattern) :
    for i in range(len(pattern)-1) :
        n = 0
        i_min, i_max = i, i+1
        while i_min >= 0 and i_max < len(pattern) :
            n += [pattern[i_min][j] != pattern[i_max][j] for j in range(len(pattern[0]))].count(True)
            i_min -= 1
            i_max +=1
            if n > 1 :
                break
        if n == 1 :
            return 100*(i+1)
    for j in range(len(pattern[0])-1) :
        n = 0
        j_min, j_max = j, j+1
        while j_min >= 0 and j_max < len(pattern[0]) :
            n += [pattern[i][j_min] != pattern[i][j_max] for i in range(len(pattern))].count(True)
            j_min -= 1
            j_max += 1
            if n > 1 :
                break
        if n == 1 :
            return j+1


if __name__ == "__main__" :
    file = open("2023/day13/input.txt")
    lines = [line[:-1] for line in file.readlines()]
    file.close()
    patterns = []
    i = 0
    while i < len(lines) :
        if lines[i] == '' :
            patterns.append(lines[:i])
            lines = lines[i+1:]
            i = 0
        else :
            i += 1
    n = 0
    for i in range(len(patterns)) :
        n += value(patterns[i])
    print(n)