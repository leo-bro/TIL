def solution(quiz):
    answer = []
    for q in quiz:
        qs = q.split(" = ")
        print(qs)
        print(eval(qs[0]))
        print(qs[1])
        print(eval(qs[0]) == eval(qs[1]))
        if eval(qs[0]) == qs[1]:
            answer.append("O")
        elif eval(qs[0]) != qs[1]:
            answer.append("X")
    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
