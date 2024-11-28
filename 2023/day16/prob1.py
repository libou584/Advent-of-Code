def next(map, i, j, direction) :
    if direction == "up" :
        i -= 1
    elif direction == "right" :
        j += 1
    elif direction == "down" :
        i += 1
    elif direction == "left" :
        j -= 1
    if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]) :
        return []
    n_dir = [direction]
    tile = map[i][j]
    if tile == "/" :
        if direction == "up" :
            n_dir = ["right"]
        elif direction == "left" :
            n_dir = ["down"]
        elif direction == "down" :
            n_dir = ["right"]
        elif direction == "right" :
            n_dir = ["up"]
    elif tile == "\\" :
        if direction == "up" :
            n_dir = ["left"]
        elif direction == "left" :
            n_dir = ["up"]
        elif direction == "down" :
            n_dir = ["right"]
        elif direction == "right" :
            n_dir = ["down"]
    elif tile == "|" and (direction == "left" or direction == "right") :
        n_dir = ["up", "down"]
    elif tile == "-" and (direction == "up" or direction == "down") :
        n_dir = ["left", "right"]
    return [(i, j, dir) for dir in n_dir]


def print_map(map, marqued) :
    for i in range(len(map)) :
        for j in range(len(map[0])) :
            if (i, j) in marqued :
                print("#", end = "")
            else :
                print(".", end = "")
        print("")


if __name__ == "__main__" : # This works for the example but not for my input, i don't know why
    file = open("2023/day16/sample.txt")
    map = [[c for c in line[:-1]] for line in file.readlines()]
    file.close()
    marqued = [(0, 0)]
    existed = {(0, 0, "right")}
    beams = [(0, 0, "right")]
    while len(beams) > 0 :
        beam = beams.pop(0)
        if (beam[0], beam[1]) not in marqued :
            marqued.append((beam[0], beam[1]))
        existed.add(beam)
        n_beams = next(map, beam[0], beam[1], beam[2])
        for beam in n_beams :
            if beam not in existed :
                beams.append(beam)
    # print_map(map, marqued)
    # print(marqued)
    print(len(marqued))