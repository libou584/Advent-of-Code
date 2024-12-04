def number(map, i, j) :
    n = 0
    if i >= 3 and map[i-1][j] == 'M' and map[i-2][j] == 'A' and map[i-3][j] == 'S' :
        n += 1
    if i < len(map) - 3 and map[i+1][j] == 'M' and map[i+2][j] == 'A' and map[i+3][j] == 'S' :
        n += 1
    if j >= 3 and map[i][j-1] == 'M' and map[i][j-2] == 'A' and map[i][j-3] == 'S' :
        n += 1
    if j < len(map[0]) - 3 and map[i][j+1] == 'M' and map[i][j+2] == 'A' and map[i][j+3] == 'S' :
        n += 1
    if i >= 3 and j >= 3 and map[i-1][j-1] == 'M' and map[i-2][j-2] == 'A' and map[i-3][j-3] == 'S' :
        n += 1
    if i < len(map) - 3 and j < len(map[0]) - 3 and map[i+1][j+1] == 'M' and map[i+2][j+2] == 'A' and map[i+3][j+3] == 'S' :
        n += 1
    if i >= 3 and j < len(map[0]) - 3 and map[i-1][j+1] == 'M' and map[i-2][j+2] == 'A' and map[i-3][j+3] == 'S' :
        n += 1
    if i < len(map) - 3 and j >= 3 and map[i+1][j-1] == 'M' and map[i+2][j-2] == 'A' and map[i+3][j-3] == 'S' :
        n += 1
    return n


if __name__ == "__main__" :
    file = open("2024/day04/input.txt")
    map = [[c for c in line[:-1]] for line in file.readlines()]
    file.close()
    n = 0
    for i in range(len(map)) :
        for j in range(len(map[0])) :
            if map[i][j] == 'X' :
                n += number(map, i, j)
    print(n)