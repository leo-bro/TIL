def solution(arr):
    answer = []
    stk = []
    i = 0
    while i < len(arr):
        if stk == []:
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk = stk[0:-1]
        elif stk[-1] != arr[i]:
            stk.append(arr[i])
        i = i + 1
    answer = [-1] if stk == [] else stk
    return answer


def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])

    return stk or [-1]


print(solution([1, 1, 3, 3, 0, 1, 1]))
