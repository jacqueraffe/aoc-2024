f = open("/Users/jacqueline/Developer/aoc-2024/day01/day01-input.txt", "r")
arr1 = []
arr2 = []
for x in f:
    line = x.split(" ")
    arr1.append(int(line[0]))
    arr2.append(int(line[3]))
arr1.sort()
arr2.sort()
dist = 0
for i in range(len(arr1)):
    print(arr2[i] - arr1[i], arr2[i], arr1[i])
    dist += abs(arr2[i] - arr1[i])
print(dist)
