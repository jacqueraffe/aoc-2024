f = open("/Users/jacqueline/Developer/aoc-2024/day02/day02-input.txt", "r")


def check_if_safe(line):
    safe = True
    increasing = True
    if int(line[0]) > int(line[1]):
        increasing = False
    for i in range(len(line) - 1):
        a = int(line[i])
        b = int(line[i + 1])
        diff = abs(a - b)
        if diff not in [1, 2, 3]:
            safe = False
            break
        if increasing and a > b:
            safe = False
            break
        if not increasing and a < b:
            safe = False
            break
    if safe:
        return True


def variation(x):
    arrs = []
    for i in range(len(x)):
        arr = []
        for j in range(len(x)):
            if i != j:
                arr.append(x[j])
        arrs.append(arr)
    print(arrs)
    return arrs


safeReports = 0

for x in f:
    line = x.split(" ")
    if check_if_safe(line):
        safeReports += 1
    else:
        for y in variation(line):
            if check_if_safe(y):
                safeReports += 1
                break


print(safeReports)
