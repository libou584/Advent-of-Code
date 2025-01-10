import re


def get_dims(lines) :
    dims = []
    for line in lines :
        matches = re.findall("\d+", line)
        dims.append([int(n) for n in matches])
    return dims


def get_perimeter(dim) :
    return [2*dim[0] + 2*dim[1], 2*dim[1] + 2*dim[2], 2*dim[2] + 2*dim[0]]


if __name__ == "__main__" :
    file = open("2015/day02/input.txt")
    lines = file.readlines()
    file.close()
    n = 0
    dims = get_dims(lines)
    for dim in dims :
        perimeters = get_perimeter(dim)
        n += min(perimeters) + dim[0]*dim[1]*dim[2]
    print(n)