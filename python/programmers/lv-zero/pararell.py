def solution(dots):
    slope = []
    for i in range(3):
        for j in range(1, 4 - i):
            if (dots[i][0] - dots[i + j][0]) == 0:
                slope.append()
            slope.append((dots[i][1] - dots[i + j][1]) / (dots[i][0] - dots[i + j][0]))
    return 1 if len(slope) != len(set(slope)) else 0
