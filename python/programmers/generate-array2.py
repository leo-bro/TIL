def solution(l, r):
    answer = []
    answer = [
        i for i in range(l, r + 1) if set(list(f"{i}")) in [{"0"}, {"5"}, {"0", "5"}]
    ]
    if answer == []:
        answer = [-1]
    return answer
