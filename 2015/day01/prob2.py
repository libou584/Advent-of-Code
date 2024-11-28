if __name__ == "__main__" :
    file = open("2015/day01/input.txt")
    line = file.read()
    file.close()
    n = 0
    for i in range(len(line)) :
        c = line[i]
        if c == "(" :
            n += 1
        else :
            n -= 1
        if n == -1 :
            print(i+1)
            break