import re


def valid_seed(seed, seeds) :
    for i in range(len(seeds)//2) :
        if seeds[2*i] <= seed and seed < seeds[2*i] + seeds[2*i + 1] :
            return True
    return False


def valid_location(location, maps, seeds) :
    key = location
    for i in range(len(maps) - 1, -1, -1) :
        map = maps[i]
        for line in map :
            if line[0] <= key and key <= line[0] + line[2] - 1 :
                key = line[1] - line[0] + key
                break
    return valid_seed(key, seeds)


if __name__ == "__main__" :
    file = open("2023/day05/input.txt")
    lines = file.readlines()
    file.close()
    seeds = [int(n) for n in re.findall("\d+", lines[0])]
    maps = []
    cond = True
    if cond :
        map1 = []
        for i in range(3, 35) :
            map1.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map1)
        map2 = []
        for i in range(37, 55) :
            map2.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map2)
        map3 = []
        for i in range(57, 105) :
            map3.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map3)
        map4 = []
        for i in range(107, 140) :
            map4.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map4)
        map5 = []
        for i in range(142, 178) :
            map5.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map5)
        map6 = []
        for i in range(180, 209) :
            map6.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map6)
        map7 = []
        for i in range(211, 239) :
            map7.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map7)
    else :
        map1 = []
        for i in range(3, 5) :
            map1.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map1)
        map2 = []
        for i in range(7, 10) :
            map2.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map2)
        map3 = []
        for i in range(12, 16) :
            map3.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map3)
        map4 = []
        for i in range(18, 20) :
            map4.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map4)
        map5 = []
        for i in range(22, 25) :
            map5.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map5)
        map6 = []
        for i in range(27, 29) :
            map6.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map6)
        map7 = []
        for i in range(31, 33) :
            map7.append([int(n) for n in re.findall("\d+", lines[i])])
        maps.append(map7)
    location = 0
    while True :
        if valid_location(location, maps, seeds) :
            print(location)
            break
        location += 1
        if location%100000 == 0 :
            print(location)