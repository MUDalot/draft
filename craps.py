from random import randint

player1: int = 0
player2: int = 0

for i in range(1, 100001):
    x: int = randint(1, 6)
    y: int = randint(1, 6)

    num = x + y
    if x + y == 7 or x + y == 11:
        player1 += 1
        continue
    elif x + y == 2 or x + y == 3 or x + y == 12:
        player2 += 1
        continue

    while True:
        x = randint(1, 6)
        y = randint(1, 6)
        if num == x + y:
            player1 += 1
            break
        elif 7 == x + y:
            player2 += 1
            break
print("玩家赢了%d局\n庄家赢了%d局" % (player1, player2))
