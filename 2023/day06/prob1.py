import math


def f(T, D) :
    # -t*(t-T) - D
    d = T**2 - 4*D
    return math.ceil((T + d**0.5)/2 - 1) - math.floor((T - d**0.5)/2 + 1) + 1


if __name__ == "__main__" :
    races = [[56, 334], [71, 1135], [79, 1350], [99, 2430]]
    races2 = [[7, 9], [15, 40], [30, 200]]
    n = 1
    for (T, D) in races :
        n *= f(T, D)
    print(n)