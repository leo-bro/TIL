def solution(my_string, m, c):
    answer = ""
    for i in range(int(len(my_string) / m)):
        answer += my_string[m * i : m * (i + 1)][c - 1]
    return answer


def solution(s, m, c):
    return s[c - 1 :: m]
