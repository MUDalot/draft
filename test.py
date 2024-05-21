#############################
#水仙花数
num = int(input('num='))
a = []
temp = num
while True:
    a.append(temp % 10)
    temp //= 10
    if temp <= 0:
        break
print(a)

sum_of_num: int = 0

for x in range(a.__len__()):
    sum_of_num += a[x] ** 3
print('%d各位数字之和为%d' % (num, sum_of_num))
print('该数字', end='')
if sum_of_num != num:
    print('不', end='')
print("是水仙花数")
#############################