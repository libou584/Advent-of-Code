import re


def hash(s) :
    n = 0
    for c in s :
        n += ord(c)
        n *= 17
        n %= 256
    return n


def performOp(boxes, seq) :
    label = re.search("\w+", seq).group()
    index = hash(label)
    operation = re.search("(=|-)", seq).group()
    if operation == "-" :
        for i in range(len(boxes[index])) :
            if boxes[index][i][0] == label :
                boxes[index].pop(i)
                break
    else :
        length = int(re.search("\d", seq).group())
        alreadyIn = False
        for i in range(len(boxes[index])) :
            if boxes[index][i][0] == label :
                alreadyIn = True
                boxes[index][i] = (label, length)
                break
        if not alreadyIn :
            boxes[index].append((label, length))
    return boxes


def TFP(boxes) :
    n = 0
    for i in range(len(boxes)) :
        for j in range(len(boxes[i])) :
            n += (i+1)*(j+1)*boxes[i][j][1]
    return n


if __name__ == "__main__" :
    file = open("2023/day15/input.txt")
    seqs = file.read().split(",")
    file.close()
    boxes = [[] for i in range(256)]
    for seq in seqs :
        boxes = performOp(boxes, seq)
    print(TFP(boxes))