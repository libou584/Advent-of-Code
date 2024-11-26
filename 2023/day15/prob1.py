def hash(s) :
    n = 0
    for c in s :
        n += ord(c)
        n *= 17
        n %= 256
    return n


if __name__ == "__main__" :
    file = open("2023/day15/input.txt")
    seqs = file.read().split(",")
    file.close()
    n = 0
    for seq in seqs :
        n += hash(seq)
    print(n)