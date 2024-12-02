def is_safe(report, removed = False) :
    if report[0] == report[1] :
        return False if removed else is_safe(report[1:], True) or is_safe(report[:1] + report[2:], True)
    inc = report[1] > report[0]
    if inc :
        for i in range(len(report)-1) :
            if report[i+1] <= report[i] :
                if removed :
                    return False
                else :
                    for i in range(len(report)) :
                        if is_safe(report[:i] + report[i+1:], True) :
                            return True
                    return False
            diff = report[i+1] - report[i]
            if diff > 3 :
                if removed :
                    return False
                else :
                    for i in range(len(report)) :
                        if is_safe(report[:i] + report[i+1:], True) :
                            return True
                    return False
    else :
        for i in range(len(report)-1) :
            if report[i+1] >= report[i] :
                if removed :
                    return False
                else :
                    for i in range(len(report)) :
                        if is_safe(report[:i] + report[i+1:], True) :
                            return True
                    return False
            diff = report[i] - report[i+1]
            if diff > 3 :
                if removed :
                    return False
                else :
                    for i in range(len(report)) :
                        if is_safe(report[:i] + report[i+1:], True) :
                            return True
                    return False
    return True


if __name__ == "__main__" :
    file = open("2024/day02/input.txt")
    reports = [[int(n) for n in line.split()] for line in file.readlines()]
    file.close()
    n = 0
    for report in reports :
        safe = is_safe(report)
        n += 1 if safe else 0
    print(n)