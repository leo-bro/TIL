def solution(myString, pat):
    d = {"A": "B", "B": "A"}
    myString_table = myString.maketrans(d)
    answer = 1 if pat in myString.translate(myString_table) else 0
    return answer
