def solution(todo_list, finished):
    answer = []
    dic = dict(zip(todo_list, finished))
    answer = [k for k, v in dic.items() if v == False]
    return answer
