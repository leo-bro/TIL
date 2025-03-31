def solution(rank, attendance):
    answer = 0
    arr = [(i, (r, a)) for i, (r, a) in enumerate(zip(rank, attendance))]

    # Filter elements where a is True and sort by r in ascending order
    filtered_sorted_arr = sorted([x for x in arr if x[1][1]], key=lambda x: x[1][0])

    # Extract the indices of the top 3 elements
    if len(filtered_sorted_arr) >= 3:
        a, b, c = (
            filtered_sorted_arr[0][0],
            filtered_sorted_arr[1][0],
            filtered_sorted_arr[2][0],
        )
        answer = 10000 * a + 100 * b + c
    return answer


def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]


print(solution([1, 3, 12, 4, 9, 6], [True, False, True, False, True, False]))
