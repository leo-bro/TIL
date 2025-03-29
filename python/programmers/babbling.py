def solution(babbling):
    answer = 0
    able = ["aya", "ye", "woo", "ma"]
    for w in babbling:
        for i in range(len(able)):
            w = w.replace(able[i], " ")
            print(w)
        if w in "    ":
            answer += 1
    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))  # 1
