f = open("/Users/jacqueline/Developer/aoc-2024/day01/day01-input.txt", "r")
arr1 = []
arr2 = []
for x in f:
    line = x.split(" ")
    arr1.append(int(line[0]))
    arr2.append(int(line[3]))
arr1.sort()
arr2.sort()
dict = {}
for i in arr2:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1
total = 0
print(arr1)
for i in arr1:
    if i in dict:
        total += dict[i] * i
print(total)
