def getNumber(s) :
    digits = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    n = len(s)
    for i in range(n) :
        if 48 <= ord(s[i]) and ord(s[i]) <= 57 :
            d = int(s[i])
            break
        else :
            for digit in digits :
                if n - i - 1 >= len(digit) and s[i:i+len(digit)] == digit :
                    d = digits[digit]
                    break
            else :
                continue
            break
    for i in range(n - 1, -1, -1) :
        if 48 <= ord(s[i]) and ord(s[i]) <= 57 :
            u = int(s[i])
            break
        else :
            for digit in digits :
                if n - i - 1 >= len(digit) and s[i:i+len(digit)] == digit :
                    u = digits[digit]
                    break
            else :
                continue
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