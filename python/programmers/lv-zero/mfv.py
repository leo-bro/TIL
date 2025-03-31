def solution(array):
    answer = []
    num = list(set(array))
    cnt = [0] * len(set(array))
    for i, n in enumerate(num):
        for a in array:
            if n == a:
                cnt[i] += 1
    m = max(cnt)
    for i, c in enumerate(cnt):
        if c == m:
            answer += [num[i]]
    answer = -1 if len(answer) > 1 else answer[0]
    return answer


def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0:
            return a
    return -1


print(solution([1, 2, 3, 4, 5, 5, 5, 5, 5]))  # 5
print(solution([1, 2, 3, 4, 5, 5, 5, 5, 4]))  # -1
