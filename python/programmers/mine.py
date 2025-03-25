def solution(board):
    n = len(board)
    mine = [[0] * n for i in range(n)]
    di = [0, 0, 0, -1, -1, -1, 1, 1, 1]
    dj = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(9):
                    ii = i + di[k]
                    jj = j + dj[k]
                    if 0 <= ii < n and 0 <= jj < n:
                        mine[ii][jj] += 1
    return sum([mine[i].count(0) for i in range(n)])


print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)  # 0
