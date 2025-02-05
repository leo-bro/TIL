def solution(arr):
    answer = 0
    xarr = []
    xarr.append(arr.copy())
    while True:
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        if arr in xarr:
            answer = len(xarr) - 1
            break
        xarr.append(arr.copy())
    return answer


print(solution([4, 7, 12, 16, 20]))
