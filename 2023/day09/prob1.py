

def value(line) :
    m = [line]
    while any(n != 0 for n in m[-1]) :
        next = []
        for i in range(1, len(m[-1])) :
            next.append(m[-1][i] - m[-1][i-1])
        m.append(next)
    m[-1].append(0)
    for j in range(len(m)-2, -1, -1) :
        m[j].append(m[j+1][-1] + m[j][-1])
    return m[0][-1]


if __name__ == "__main__" :
    file = open("2023/day09/input.txt")
    lines = file.readlines()
    file.close()
    n = 0
    for line in lines :
        n += value([int(m) for m in line.split()])
    print(n)