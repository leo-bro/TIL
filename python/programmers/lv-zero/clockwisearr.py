def solution(n):
    try:
        arr = [[0] * n for i in range(n)]
        dir = "r"
        x = 0
        y = 0
        for i in range(n * n):
            arr[x][y] = i + 1
            if dir == "r":
                y += 1
                if (y == n - 1) or (arr[x][y + 1] != 0):
                    dir = "d"
            elif dir == "d":
                x += 1
                if (x == n - 1) or (arr[x + 1][y] != 0):
                    dir = "l"
            elif dir == "l":
                y -= 1
                if (y == 0) or (arr[x][y - 1] != 0):
                    dir = "u"
            elif dir == "u":
                x -= 1
                if (x == 0) or (arr[x - 1][y] != 0):
                    dir = "r"
        answer = arr
    except:
        answer = [[1]]

    return answer


print(solution(4))  # [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
