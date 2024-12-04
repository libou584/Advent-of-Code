def number(map, i, j) :
    n = 0
    if map[i-1][j-1] == 'M' and map[i+1][j+1] == 'S' and map[i+1][j-1] == 'M' and map[i-1][j+1] == 'S' :
        n += 1
    if map[i-1][j-1] == 'M' and map[i+1][j+1] == 'S' and map[i+1][j-1] == 'S' and map[i-1][j+1] == 'M' :
        n += 1
    if map[i-1][j-1] == 'S' and map[i+1][j+1] == 'M' and map[i+1][j-1] == 'M' and map[i-1][j+1] == 'S' :
        n += 1
    if map[i-1][j-1] == 'S' and map[i+1][j+1] == 'M' and map[i+1][j-1] == 'S' and map[i-1][j+1] == 'M' :
        n += 1
    return n


if __name__ == "__main__" :
    file = open("2024/day04/input.txt")
    map = [[c for c in line[:-1]] for line in file.readlines()]
    file.close()
    n = 0
    for i in range(1, len(map) - 1) :
        for j in range(1, len(map[0]) - 1) :
            if map[i][j] == 'A' :
                n += number(map, i, j)
    print(n)