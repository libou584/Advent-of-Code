def next(map, p, p0) :
    i, j = p
    i0, j0 = p0
    if map[i][j] == '|' :
        if i0 != i-1 :
            return i-1, j
        return i+1, j
    elif map[i][j] == '-' :
        if j0 != j-1 :
            return i, j-1
        return i, j+1
    elif map[i][j] == 'L' :
        if i0 != i-1 :
            return i-1, j
        return i, j+1
    elif map[i][j] == 'J' :
        if i0 != i-1 :
            return i-1, j
        return i, j-1
    elif map[i][j] == '7' :
        if i0 != i :
            return i, j-1
        return i+1, j
    elif map[i][j] == 'F' :
        if i0 != i :
            return i, j+1
        return i+1, j


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
    p10, p20 = (i0, j0), (i0, j0)
    p1, p2 = (i0-1, j0), (i0+1, j0) # only for my input file
    n = 1
    while p1 != p2 :
        temp1 = p1
        p1 = next(map, p1, p10)
        p10 = temp1
        temp2 = p2
        p2 = next(map, p2, p20)
        p20 = temp2
        n += 1
    print(n)