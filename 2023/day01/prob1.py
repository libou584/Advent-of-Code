def getNumber(s) :
    n = len(s)
    for i in range(n) :
        if 48 <= ord(s[i]) and ord(s[i]) <= 57 :
            d = int(s[i])
            break
    for i in range(n - 1, -1, -1) :
        if 48 <= ord(s[i]) and ord(s[i]) <= 57 :
            u = int(s[i])
            break
    return 10*d + u


if __name__ == "__main__" :
    file = open("2023/day01/input.txt", "r")
    lines = file.readlines()
    file.close()
    n = 0
    for line in lines :
        n += getNumber(line)
    print(n)