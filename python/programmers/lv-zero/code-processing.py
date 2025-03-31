def solution(code):
    answer = ""
    ret = ""
    mode = 0
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == "1":
                mode = 1
            else:
                ret += code[idx] * int(idx % 2 == 0)
        elif mode == 1:
            if code[idx] == "1":
                mode = 0
            else:
                ret += code[idx] * int(idx % 2 == 1)

    answer = ret if ret != "" else "EMPTY"
    return answer
