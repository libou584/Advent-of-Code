def antinode(map, antenna1, antenna2) :
    res = []
    i0, j0 = min(antenna1[0], antenna2[0]), min(antenna1[1], antenna2[1]) # TODO : change this for the real antinodes
    i1, j1 = max(antenna1[0], antenna2[0]), max(antenna1[1], antenna2[1])
    antinode1 = (2*i0 - i1, 2*j0 - j1)
    antinode2 = (2*i1 - i0, 2*j1 - j0)
    if antinode1[0] >= 0 and antinode1[1] >= 0 :
        res.append(antinode1)
    if antinode2[0] < len(map) and antinode2[1] < len(map[0]) :
        res.append(antinode2)
    return res


if __name__ == "__main__" :
    file = open("2024/day08/input.txt")
    map = [line[:-1] for line in file.readlines()]
    file.close()
    antennas = {}
    for i in range(len(map)) :
        for j in range(len(map[0])) :
            c = map[i][j]
            if c != '.' :
                if c in antennas :
                    antennas[c].append((i, j))
                else :
                    antennas[c] = [(i, j)]
    antinodes = []
    for c in antennas :
        list = antennas[c]
        for k in range(len(list) - 1) :
            for l in range(k+1, len(list)) :
                res = antinode(map, list[k], list[l])
                for anti in res :
                    if anti not in antinodes :
                        antinodes.append(anti)
    print(len(antinodes))
