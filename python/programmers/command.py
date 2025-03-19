def solution(keyinput, board):
    pos = [0, 0]
    xx = (board[0] - 1) / 2
    yy = (board[1] - 1) / 2
    for cmd in keyinput:
        if cmd == "left":
            pos[0] -= 1 if pos[0] - 1 >= -xx else 0
        elif cmd == "right":
            pos[0] += 1 if pos[0] + 1 <= xx else 0
        elif cmd == "up":
            pos[1] += 1 if pos[1] + 1 <= yy else 0
        elif cmd == "down":
            pos[1] -= 1 if pos[1] - 1 >= -yy else 0
    return pos


print(solution(["down", "down", "down", "down", "down"], [7, 9]))  # [0, -1]
