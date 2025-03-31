def solution(strArr):
    strl = []
    count = {}
    for s in strArr:
        strl.append(len(s))
    for value in strl:
        try:
            count[value] += 1
        except:
            count[value] = 1
    answer = max(count)
    return answer


def solution(strArr):
    d = {}

    for i in strArr:
        d[len(i)] = d.get(len(i), 0) + 1

    return max(d.values())


print(solution(["a", "de", "fgh", "ijk"]))  # 3
