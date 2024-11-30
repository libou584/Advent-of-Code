import copy


#   1
# 2 . 0
#   3


class Path :
    
    def __init__(self, path = None) :
        if path is None :
            self.direction = None
            self.same_dir = 0
            self.list = [(0, 0)]
            self.heat_loss = 0
        else :
            self.direction = path.direction
            self.same_dir = path.same_dir
            self.list = copy.deepcopy(path.list)
            self.heat_loss = path.heat_loss
    
    def extend(self, map, heat_map) :
        i, j = self.list[-1]
        if self.heat_loss >= heat_map[i][j] :
            return []
        heat_map[i][j] = self.heat_loss
        if self.direction is None :
            directions = [0, 3]
        else :
            directions = [self.direction] if self.same_dir <= 3 else []
            directions.append((self.direction + 1)%4)
            directions.append((self.direction - 1)%4)
        paths = []
        for dir in directions :
            if dir == 0 :
                j += 1
            elif dir == 1 :
                i -= 1
            elif dir == 2 :
                j -= 1
            elif dir == 3 :
                i += 1
            if (i, j) not in self.list and i >= 0 and i < len(map) and j >= 0 and j < len(map[0]) :
                path = Path(self)
                path.direction = dir
                if dir == self.direction :
                    path.same_dir += 1
                else :
                    path.same_dir = 0
                path.list.append((i, j))
                path.heat_loss += map[i][j]
                paths.append(path)
        return paths


if __name__ == "__main__" : # TODO : Start over !
    file = open("2023/day17/sample.txt")
    map = [[int(n) for n in line[:-1]] for line in file.readlines()]
    file.close()
    heap = []
    path = Path()
    stack = [path]
    heat_map = [[196000 for i in range(len(map))] for j in range(len(map[0]))]
    n = 0
    while stack :
        n += 1
        if n%1000 == 0 :
            # print(n)
            pass
        path = stack.pop()
        if path.list[-1] == (len(map)-1, len(map[0])-1) :
            print(path.heat_loss, path.list)
            # break
        paths = path.extend(map, heat_map)
        del path
        for path in paths :
            stack.append(path)
    print(heat_map)