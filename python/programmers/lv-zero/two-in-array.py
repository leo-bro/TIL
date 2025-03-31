def solution(arr):
    answer = []
    two = []
    for i in range(len(arr)):
        if arr[i] == 2:
            two.append(i)
    if 2 in arr:
        answer = arr[two[0] : two[-1] + 1]
    else:
        answer = [-1]
    return answer


def solution(arr):
    answer = []
    two = []
    for i in range(len(arr)):
        if arr[i] == 2:
            two.append(i)
    if 2 in arr:
        answer = arr[two[0] : two[-1] + 1]
    else:
        answer = [-1]
    return answer
