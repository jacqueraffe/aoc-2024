f = open("/Users/jacqueline/Developer/aoc-2024/day02/day02-input.txt", "r")
safeReports = 0
for x in f:
    line = x.split(" ")
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
            print("diff not right", line, a, b, diff)
            break
        if increasing and a > b:
            safe = False
            print(increasing, line, a, b)
            break
        if not increasing and a < b:
            safe = False
            print(increasing, line, a, b)
            break
    if safe:
        safeReports += 1
        print("safe", line)

print(safeReports)
