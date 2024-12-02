def is_safe(report) :
    if report[0] == report[1] :
        return False
    inc = report[1] > report[0]
    if inc :
        for i in range(len(report)-1) :
            if report[i+1] <= report[i] :
                return False
            diff = report[i+1] - report[i]
            if diff > 3 :
                return False
    else :
        for i in range(len(report)-1) :
            if report[i+1] >= report[i] :
                return False
            diff = report[i] - report[i+1]
            if diff > 3 :
                return False
    return True


if __name__ == "__main__" :
    file = open("2024/day02/input.txt")
    reports = [[int(n) for n in line.split()] for line in file.readlines()]
    file.close()
    n = 0
    for report in reports :
        n += 1 if is_safe(report) else 0
    print(n)