def solution(rank, attendance):
    answer = 0
    arr = [r for r, a in zip(rank, attendance) if a == True]
    darr = dict(zip(arr, range(1, len(arr) + 1)))
    darr2 = dict(sorted(darr.items()))
    a, b, c = darr2.values()[0:2]
    answer = 10000 * a + 100 * b + c
    return answer


print(solution([1, 3, 12, 4, 9, 6], [True, False, True, False, True, False]))
