def solution(arr):
    answer = [[]]
    x = len(arr)
    y = len(arr[0])
    if x > y:
        for i in range(x):
            arr[i] += (x - y) * [0]
    elif x < y:
        while len(arr) < y:
            arr += [y * [0]]
    answer = arr
    return answer
