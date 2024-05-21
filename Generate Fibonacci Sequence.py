import array as arr

et: int = int(input("请输入生成斐波那契数列的个数:"))
if et <= 0:
    print("error")
elif et == 1:
    print("1")
else:
    s: arr = [1, 1]
    for i in range(2, et):
        s.append(s[i - 1] + s[i - 2])

    print(s)
