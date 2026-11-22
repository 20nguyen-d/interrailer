n = 16

score = []
for i in range(n):
    score.append([0] * n)
score[0][5] = 1

board = []
for i in range(n):
    board.append([1] * n)
board[2][2] = 0
board[2][3] = 0
board[3][2] = 0
board[3][3] = 0


for x in range(n):
    for y in range(n - 1, -1, -1):
        if board[x][y] == 1:
            if x == 0 or y == n - 1:
                score[x][y] = 1
            else:
                score[x][y] = score[x - 1][y] + score[x][y + 1]

for y in range(n - 1, -1, -1):
    print(' '.join([str(v) for v in score[y][::-1]]))
