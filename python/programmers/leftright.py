def solution(str_list):
    answer = []
    for i, s in enumerate(str_list):
        if s == "l":
            answer = str_list[0:i]
            break
        elif s == "r":
            answer = str_list[i + 1 : :]
            break
    return answer


print(solution(["u", "u", "l", "r"]))
