def solution(my_string, indices):
    str2dict = {i: my_string[i] for i in range(len(my_string))}
    new_string = [str2dict[i] for i in range(len(my_string)) if i not in indices]
    answer = "".join(new_string)
    return answer


print(solution("abcde", [1, 3]))
