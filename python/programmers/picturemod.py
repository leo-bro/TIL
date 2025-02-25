def solution(picture, k):
    answer = []
    for s in picture:
        ss = ""
        for a in list(s):
            ss += k * a
        answer += k * [ss]
    return answer


print(solution(["x.x", ".x.", "x.x"], 3))
