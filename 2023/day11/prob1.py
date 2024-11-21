def expand(m) :
    i = 0
    while i < len(m) :
        if all([c == '.' for c in m[i]]) :
            m = m[:i] + [m[i], m[i]] + m[i+1:]
            i += 2
        else :
            i += 1
    j = 0
    while j < len(m[0]) :
        if all([c == '.' for c in [m[i][j] for i in range(len(m))]]) :
            for i in range(len(m)) :
                m[i] = m[i][:j] + ['.', '.'] + m[i][j+1:]
            j += 2
        else :
            j += 1
    return m


def stars(m) :
    stars = []
    for i in range(len(m)) :
        for j in range(len(m[0])) :
            if m[i][j] == '#' :
                stars.append((i, j))
    return stars


def print_(m) :
    for line in m :
        print(line)


if __name__ == "__main__" :
    file = open("2023/day11/input.txt")
    m = [[c for c in line[:-1]] for line in file.readlines()]
    file.close()
    stars = stars(expand(m))
    n = 0
    for i in range(len(stars)-1) :
        for j in range(i+1, len(stars)) :
            n += abs(stars[i][0] - stars[j][0]) + abs(stars[i][1] - stars[j][1])
    print(n)