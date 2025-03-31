def solution(A, B):
    if A == B:
        return 0
    else:
        for i in range(len(A)):
            A = A[-1] + A[1:]
            print(A)
            if A == B:
                return i
                break
            else:
                continue
        return -1


(solution("abcde", "cdeab"))  # 2
