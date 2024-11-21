def expand(m) :
    I = []
    J = []
    for i in range(len(m)) :
        if all([c == '.' for c in m[i]]) :
            I.append(i)
    for j in range(len(m[0])) :
        if all([c == '.' for c in [m[i][j] for i in range(len(m))]]) :
            J.append(j)
    return I, J


def stars(m) :
    stars = []
    for i in range(len(m)) :
        for j in range(len(m[0])) :
            if m[i][j] == '#' :
                stars.append((i, j))
    return stars


if __name__ == "__main__" :
    file = open("2023/day11/input.txt")
    m = [[c for c in line[:-1]] for line in file.readlines()]
    file.close()
    I, J = expand(m)
    stars = stars(m)
    n = 0
    for i in range(len(stars)-1) :
        for j in range(i+1, len(stars)) :
            n += abs(stars[i][0] - stars[j][0]) + abs(stars[i][1] - stars[j][1])
            for row in I :
                if stars[i][0] < row and row < stars[j][0] :
                    n += 999999
            min_ = min(stars[i][1], stars[j][1])
            max_ = max(stars[i][1], stars[j][1])
            for col in J :
                if min_ < col and col < max_ :
                    n += 999999
    print(n)