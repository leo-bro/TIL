def solution(my_string, num1, num2):
    ms = list(my_string)
    answer = list(my_string)
    answer[num1] = ms[num2]
    answer[num2] = ms[num1]
    answer = "".join(answer)
    return answer
