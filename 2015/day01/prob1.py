if __name__ == "__main__" :
    file = open("2015/day01/input.txt")
    line = file.read()
    file.close()
    n = 0
    for c in line :
        if c == "(" :
            n += 1
        else :
            n -= 1
    print(n)