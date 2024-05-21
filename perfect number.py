import array
et: int = int(input("查询至的最大数："))

note: array = [[0]]
for i in range(1, et + 1):
    note.append([1])

for i in range(2, et + 1):
    for k in range(1, et // i + 1):
        note[k * i].append(i)

num_of_pn: int = 0
for i in range(1,et + 1):
    current_sum: int = 0
    for j in range(len(note[i])):
        current_sum += note[i][j]
    if current_sum == 2 * i:
        print(i)
        num_of_pn += 1
print("范围内发现了%d个完美数" % num_of_pn)

