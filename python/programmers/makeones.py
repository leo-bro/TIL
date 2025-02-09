def solution(num_list):
    answer = 0
    cnt = []
    for num in num_list:
        count = 0
        while num > 1:
            if num % 2 == 0:
                num = num / 2
                count += 1
            elif num % 2 == 1:
                num = (num - 1) / 2
                count += 1
        cnt.append(count)
    answer = sum(cnt)
    return answer


def cnt(x):
    answer = 0
    while x > 1:
        if x % 2 == 0:
            x = x / 2
            answer += 1
        else:
            x = (x - 1) / 2
            answer += 1
    return answer


def solution(num_list):
    answer = 0
    for i in num_list:
        answer += cnt(i)
    return answer
