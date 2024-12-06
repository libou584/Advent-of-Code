

#   1
# 2 . 0
#   3


class Guard :

    def __init__(self, I, J) :
        self.i = I
        self.j = J
        self.direction = 1
        self.passed = {(I, J, self.direction)}

    def move(self, map, marqued) :
        temp_i, temp_j = self.i, self.j
        if self.direction == 1 :
            self.i -= 1
        elif self.direction == 0 :
            self.j += 1
        elif self.direction == 3 :
            self.i += 1
        elif self.direction == 2 :
            self.j -= 1
        if self.i >= 0 and self.i < len(map) and self.j >= 0 and self.j < len(map[0]) :
            if map[self.i][self.j] == '#' :
                self.i = temp_i
                self.j = temp_j
                self.direction = (self.direction-1)%4
                return marqued
            else :
                if (self.i, self.j) not in marqued :
                    marqued.add((self.i, self.j))
                return marqued
        return None
    
    def move2(self, map) :
        temp_i, temp_j = self.i, self.j
        if self.direction == 1 :
            self.i -= 1
        elif self.direction == 0 :
            self.j += 1
        elif self.direction == 3 :
            self.i += 1
        elif self.direction == 2 :
            self.j -= 1
        if self.i >= 0 and self.i < len(map) and self.j >= 0 and self.j < len(map[0]) :
            if map[self.i][self.j] == '#' :
                self.i = temp_i
                self.j = temp_j
                self.direction = (self.direction-1)%4
            if (self.i, self.j, self.direction) in self.passed :
                return True
            self.passed.add((self.i, self.j, self.direction))
            return None
        return False


if __name__ == "__main__" :
    file = open("2024/day06/input.txt")
    map = [[c for c in line[:-1]] for line in file.readlines()]
    file.close()
    for i in range(len(map)) :
        for j in range(len(map[0])) :
            if map[i][j] == '^' :
                I, J = i, j
    marqued = {(I, J)}
    guard = Guard(I, J)
    while True :
        res = guard.move(map, marqued)
        if res is not None :
            marqued = res
        else :
            break
    n = 0
    for (i, j) in marqued :
        map[i][j] = '#'
        guard = Guard(I, J)
        while True :
            res = guard.move2(map)
            if res is not None :
                if res :
                    n += 1
                break
        map[i][j] = '.'
    print(n)