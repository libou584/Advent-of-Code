import re


def seed_to_location(seed, maps) :
    mapped = [seed]
    for map in maps :
        max_under = 0
        max_under_index = -1
        for i in range(len(map)) :
            line = map[i]
            if line[1] <= mapped[-1] and line[1] >= max_under :
                max_under = line[1]
                max_under_index = i
        if max_under_index >= 0 and mapped[-1] - max_under < map[max_under_index][2] :
            mapped.append(map[max_under_index][0] + mapped[-1] - max_under)
        else :
            mapped.append(mapped[-1])
    return mapped[-1]


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
    locations = []
    for seed in seeds :
        locations.append(seed_to_location(seed, maps))
    print(min(locations))