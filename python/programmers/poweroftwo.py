def isPowerOf2(n):
    return (n & (n - 1)) == 0


def solution(arr):
    answer = []
    while isPowerOf2(len(arr)) == False:
        arr.append(0)
    answer = arr
    return answer


print(solution([1, 2, 3, 4, 5, 6]))
