num_of_coin = int(input('请输入钱的总数：'))
num_of_chi = int(input('请输入鸡的总数：'))
find = False
for male in range(num_of_coin // 5):
    for female in range(num_of_chi - male + 1):
        kid = (num_of_coin - (5 * male + 3 * female)) * 3
        if male + female + kid == num_of_chi:
            find = True
            print("公鸡%d 母鸡%d 小鸡%d" % (male, female, kid))
if not find:
    print('未找到')
