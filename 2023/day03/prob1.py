
def schematic(lines) :
    symbols = ["*", "$", "/", "-", "@", "+", "&", "=", "#", "%"]
    n = 0
    for i in range(len(lines)) :
        j = 0
        while j < len(lines[i]) :
            m = ""
            if 48 <= ord(lines[i][j]) and ord(lines[i][j]) <= 57 :
                m = lines[i][j]
                j += 1
                if j < len(lines[i]) and 48 <= ord(lines[i][j]) and ord(lines[i][j]) <= 57 :
                    m += lines[i][j]
                    j += 1
                    if j < len(lines[i]) and 48 <= ord(lines[i][j]) and ord(lines[i][j]) <= 57 :
                        m += lines[i][j]
                        j += 1
                part = False
                if i != 0 :
                    for j0 in range(j-len(m)-1, j+1) :
                        if 0 < j0 and j0 < len(lines[i]) and lines[i-1][j0] in symbols :
                            part = True
                            break
                if i != len(lines) -1 :
                    for j0 in range(j-len(m)-1, j+1) :
                        if 0 < j0 and j0 < len(lines[i]) and lines[i+1][j0] in symbols :
                            part = True
                            break
                if j - len(m) - 1 != 0 and lines[i][j-len(m)-1] in symbols :
                    part = True
                if j != len(lines[i]) and lines[i][j] in symbols :
                    part = True
                if part :
                    n += int(m)
            else :
                j += 1
    return n
            

if __name__ == "__main__" :
    file = open("2023/day03/input.txt")
    lines = file.readlines()
    file.close()
    print(schematic(lines))