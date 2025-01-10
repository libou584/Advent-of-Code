import re


def get_dims(lines) :
    dims = []
    for line in lines :
        matches = re.findall("\d+", line)
        dims.append([int(n) for n in matches])
    return dims


def get_surfaces(dims) :
    surfaces = []
    for dim in dims :
        surfaces.append([dim[0]*dim[1], dim[1]*dim[2], dim[2]*dim[0]])
    return surfaces


if __name__ == "__main__" :
    file = open("2015/day02/input.txt")
    lines = file.readlines()
    file.close()
    surfaces = get_surfaces(get_dims(lines))
    n = 0
    for surface in surfaces :
        n += 2*surface[0] + 2*surface[1] + 2*surface[2] + min(surface)
    print(n)