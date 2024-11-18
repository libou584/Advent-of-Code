import math


def f(T, D) :
    # -t*(t-T) - D
    d = T**2 - 4*D
    return math.ceil((T + d**0.5)/2 - 1) - math.floor((T - d**0.5)/2 + 1) + 1


if __name__ == "__main__" :
    T, D = 56717999, 334113513502430
    print(f(T, D))