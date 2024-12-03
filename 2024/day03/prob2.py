import re


if __name__ == "__main__" :
    file = open("2024/day03/input.txt")
    prog = file.read()
    file.close()
    mult = re.findall("(mul\(\d{1,3}\,\d{1,3}\)|don\'t\(\)|do\(\))", prog)
    n = 0
    take = True
    for mul in mult :
        if mul == "do()" :
            take = True
        elif mul == "don't()" :
            take = False
        else :
            if take :
                nums = re.findall("\d{1,3}", mul)
                n += int(nums[0])*int(nums[1])
    print(n)