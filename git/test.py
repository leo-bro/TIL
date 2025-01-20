def solution(a, d, included):
    answer = 0
    n = len(included)
    numarr = [x for x in range(a, a + (n - 1) * d, d)]
    answer = sum([numarr[i] * int(included[i]) for i in range(n)])
    return answer


solution(3, 4, [True, False, False, True, True])
