def solution(my_string):
    answer = ""
    for s in my_string:
        if not s in answer:
            answer += s
    return answer


def solution(my_string):
    return "".join(dict.fromkeys(my_string))
