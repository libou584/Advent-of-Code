def next(map, p, p0) :
    i, j = p
    i0, j0 = p0
    if map[i][j] == '|' :
        if i0 != i-1 :
            return (i-1, j), 0
        return (i+1, j), 0
    elif map[i][j] == '-' :
        if j0 != j-1 :
            return (i, j-1), -len(map)+i
        return (i, j+1), len(map)-i-1
    elif map[i][j] == 'L' :
        if i0 != i-1 :
            return (i-1, j), 0
        return (i, j+1), len(map)-i-1
    elif map[i][j] == 'J' :
        if i0 != i-1 :
            return (i-1, j), len(map)-i-1
        return (i, j-1), 0
    elif map[i][j] == '7' :
        if i0 != i :
            return (i, j-1), -len(map)+i
        return (i+1, j), 0
    elif map[i][j] == 'F' :
        if i0 != i :
            return (i, j+1), 0
        return (i+1, j), -len(map)+i


if __name__ == "__main__" :
    file = open("2023/day10/input.txt")
    map = file.readlines()
    file.close()
    for i in range(len(map)) :
        for j in range(len(map[0])) :
            if map[i][j] == 'S' :
                i0, j0 = i, j
                break
        else :
            continue
        break
    p0 = (i0, j0)
    p = (i0+1, j) # only for my input file
    s = 0
    while p != (i0, j0) :
        temp = p
        p, n = next(map, p, p0)
        p0 = temp
        s += n
    print(s)