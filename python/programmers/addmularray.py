def solution(num_list):
    if len(num_list) >= 11:
        answer = 0
        for n in num_list:
            answer += n
    elif len(num_list) < 10:
        answer = 1
        for n in num_list:
            answer *= n
    return answer


print(
    solution([9, 9, 9, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])
)  # [1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0]
