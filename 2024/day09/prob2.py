def process(blocks) : # TODO : modify this function for the second problem
    j = 0
    for i in range(len(blocks)-1, -1, -1) :
        if i < j :
            break
        if blocks[i] != -1 :
            temp = blocks[i]
            blocks[i] = -1
            while blocks[j] != -1 :
                j += 1
            blocks[j] = temp
    return blocks


def value(blocks) :
    n = 0
    for i in range(len(blocks)) :
        if blocks[i] != -1 :
            n += i*blocks[i]
    return n


if __name__ == "__main__" :
    file = open("2024/day09/input.txt")
    line = [int(n) for n in file.read()]
    file.close()
    blocks = []
    for i in range(len(line)) :
        if i%2 == 0 :
            for j in range(line[i]) :
                blocks.append(i//2)
        else :
            for j in range(line[i]) :
                blocks.append(-1)
    blocks = process(blocks)
    print(value(blocks))