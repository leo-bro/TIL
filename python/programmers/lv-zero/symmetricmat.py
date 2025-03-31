def solution(arr):
    return int(arr == list(map(list, zip(*arr))))


print(solution([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))  # 1

arr = [[1, 2, 3], [2, 3, 4], [3, 4, 999]]
print(zip(*arr))
print(map(list, zip(*arr)))
print(list(map(list, zip(*arr))))
