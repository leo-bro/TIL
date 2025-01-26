def solution(ineq, eq, n, m):
    answer = 0
    if eq == "=":
        answer = int(eval(f"{n}{ineq}{eq}{m}"))
    elif eq == "!":
        answer = int(eval(f"{n}{ineq}{m}"))
    return answer
