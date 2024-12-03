f = open("/Users/jacqueline/Developer/aoc-2024/day03/day03-input.txt", "r")


def check_line(line):
    i = 0
    first_num_str = ""
    while i < len(line) and line[i].isdigit():
        if i >= 3:
            return 0
        first_num_str += line[i]
        i += 1
        if i >= len(line):
            return 0
    print(first_num_str)
    print(line)
    line = line[len(first_num_str) :]
    i = 1
    snd_num_str = ""
    while i < len(line) and line[i].isdigit():
        if i >= 4:
            return 0
        snd_num_str += line[i]
        i += 1
        if i >= len(line):
            return 0
    print(snd_num_str)
    if i >= len(line):
        return 0
    if line[i] == ")" and first_num_str.isdigit() and snd_num_str.isdigit():
        return int(first_num_str) * int(snd_num_str)
    return 0


total = 0
for x in f:
    lines = x.split("mul(")
    for line in lines:
        total += check_line(line)
print(total)
