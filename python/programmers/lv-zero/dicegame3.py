def solution(a, b, c, d):
    answer = 0
    dice = [a, b, c, d]
    cnt = [dice.count(i) for i in range(1, 7)]
    if max(cnt) == 4:
        p = cnt.index(4) + 1
        answer = 1111 * p
    elif max(cnt) == 3:
        p = cnt.index(3) + 1
        q = cnt.index(1) + 1
        answer = (10 * p + q) ** 2
    elif max(cnt) == 2:
        if cnt.count(1) == 0:
            p = cnt.index(2) + 1
            cnt[cnt.index(2)] = 0
            q = cnt.index(2) + 1
            answer = (p + q) * abs(p - q)
        elif cnt.count(1) != 0:
            p = cnt.index(2) + 1
            q = cnt.index(1) + 1
            cnt[cnt.index(1)] = 0
            r = cnt.index(1) + 1
            answer = q * r
    elif max(cnt) == 1:
        answer = min(dice)

    return answer
