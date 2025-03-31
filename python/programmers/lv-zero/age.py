def solution(age):
    answer = ""
    alp = list("abcdefghij".split())
    num = list(map(int, str(age)))
    answer = "".join([alp[n] for n in num])

    return answer


print(solution(10))  # ab
