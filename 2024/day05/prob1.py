import re


def ordered(update, orders) :
    for i in range(len(update)-1) :
        for j in range(i+1, len(update)) :
            n = update[i]
            m = update[j]
            if n in orders.keys() :
                for order in orders[n] :
                    if order[0] == m :
                        return False
    return True


if __name__ == "__main__" :
    file = open("2024/day05/input.txt")
    lines = file.readlines()
    file.close()
    cond = True
    if cond :
        order_lines = lines[:1176]
        updates = [[int(n) for n in line.split(',')] for line in lines[1177:]]
    else :
        order_lines = lines[:21]
        updates = [[int(n) for n in line.split(',')] for line in lines[22:]]
    orders = {}
    for line in order_lines :
        nums = [int(n) for n in re.findall("\d{2}", line)]
        if nums[0] not in orders :
            orders[nums[0]] = [(nums[0], nums[1])]
        else :
            orders[nums[0]].append((nums[0], nums[1]))
        if nums[1] not in orders :
            orders[nums[1]] = [(nums[0], nums[1])]
        else :
            orders[nums[1]].append((nums[0], nums[1]))
    n = 0
    for update in updates :
        if ordered(update, orders) :
            n += update[len(update)//2]
    print(n)