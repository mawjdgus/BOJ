import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
board = []
count = []
for a in range(N):
    board.append(str(sys.stdin.readline().strip()))
for i in range(N-7):
    for j in range(M-7):
        black = 0
        white = 0
        for n in range(i, i+8):
            for m in range(j, j+8):
                if (n+m) % 2 == 0: 
                    if board[n][m] != 'W': # B 인 경우, black + 1 
                        black += 1
                    if board[n][m] != 'B': # W 인 경우 white
                        white += 1
                else:
                    if board[n][m] != 'B': # W인 경우 black + 1
                        black += 1
                    if board[n][m] != 'W': # B인 경우 white + 1
                        white += 1
                        
        count.append(min(white, black))
print(min(count))