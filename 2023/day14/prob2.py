def slideUp(map) :
    for i in range(1, len(map)) :
        for j in range(len(map[0])) :
            if map[i][j] == 'O' :
                i0 = i-1
                while i0 >= 0 and map[i0][j] == '.' :
                    i0 -= 1
                map[i][j] = '.'
                map[i0+1][j] = 'O'
    return map


def slideLeft(map) :
    for j in range(1, len(map[0])) :
        for i in range(len(map)) :
            if map[i][j] == 'O' :
                j0 = j-1
                while j0 >= 0 and map[i][j0] == '.' :
                    j0 -= 1
                map[i][j] = '.'
                map[i][j0+1] = 'O'
    return map


def slideDown(map) :
    for i in range(len(map)-2, -1, -1) :
        for j in range(len(map[0])) :
            if map[i][j] == 'O' :
                i0 = i+1
                while i0 < len(map) and map[i0][j] == '.' :
                    i0 += 1
                map[i][j] = '.'
                map[i0-1][j] = 'O'
    return map


def slideRight(map) :
    for j in range(len(map[0])-2, -1, -1) :
        for i in range(len(map)) :
            if map[i][j] == 'O' :
                j0 = j+1
                while j0 < len(map[0]) and map[i][j0] == '.' :
                    j0 += 1
                map[i][j] = '.'
                map[i][j0-1] = 'O'
    return map


def cycle(map) :
    return slideRight(slideDown(slideLeft(slideUp(map))))


def totalLoad(map) :
    load = 0
    n = len(map)
    for i in range(len(map)) :
        load += map[i].count('O')*(n-i)
    return load


if __name__ == "__main__" : # doesn't work
    file = open("2023/day14/input.txt")
    map0 = [[c for c in line[:-1]] for line in file.readlines()]
    map = map0
    file.close()
    n = 200
    for i in range(n-1) :
        map = cycle(map)
    baseLoad = totalLoad(map)
    map = cycle(map)
    m = n
    while totalLoad(map) != baseLoad :
        # print(totalLoad(map))
        map = cycle(map)
        m += 1
    map = map0
    for i in range((1000000000%(m-n)) + n) :
        map = cycle(map)
    print(totalLoad(map))