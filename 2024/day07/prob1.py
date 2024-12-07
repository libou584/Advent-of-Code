import re


def ok(equation) :
    if equation[1] > equation[0] :
        return False
    if len(equation) == 2 :
        return equation[0] == equation[1]
    add_equation = [equation[0], equation[1] + equation[2]] + equation[3:]
    mult_equation = [equation[0], equation[1] * equation[2]] + equation[3:]
    return ok(add_equation) or ok(mult_equation)


if __name__ == "__main__" :
    file = open("2024/day07/input.txt")
    equations = [[int(n) for n in re.findall("\d+", line)] for line in file.readlines()]
    file.close()
    n = 0
    for equation in equations :
        if ok(equation) :
            n += equation[0]
    print(n)