def solution(arr, query):
    answer = []
    for q in range(len(query)):
        i = query[q]
        if q % 2 == 0:
            arr = arr[: i + 1]
        elif q % 2 == 1:
            arr = arr[i:]
    answer = arr
    return answer


def solution(arr, query):
    for k, q in enumerate(query):
        if k % 2 == 0:
            arr = arr[: q + 1]
        else:
            arr = arr[q:]
    return arr
