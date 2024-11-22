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


def totalLoad(map) :
    load = 0
    n = len(map)
    for i in range(len(map)) :
        load += map[i].count('O')*(n-i)
    return load


if __name__ == "__main__" :
    file = open("2023/day14/input.txt")
    map = [[c for c in line[:-1]] for line in file.readlines()]
    file.close()
    print(totalLoad(slideUp(map)))