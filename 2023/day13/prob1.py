def value(pattern) :
    for i in range(len(pattern)-1) :
        mirror = True
        i_min, i_max = i, i+1
        while i_min >= 0 and i_max < len(pattern) :
            if pattern[i_min] != pattern[i_max] :
                mirror = False
                break
            i_min -= 1
            i_max +=1
        if mirror :
            return 100*(i+1)
    for j in range(len(pattern[0])-1) :
        mirror = True
        j_min, j_max = j, j+1
        while j_min >= 0 and j_max < len(pattern[0]) :
            if [pattern[i][j_min] for i in range(len(pattern))] != [pattern[i][j_max] for i in range(len(pattern))] :
                mirror = False
                break
            j_min -= 1
            j_max += 1
        if mirror :
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