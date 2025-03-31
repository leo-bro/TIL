def solution(sides):
    a = max(sides)
    sides.pop(sides.index(max(sides)))
    [b, c] = sides
    answer = 1 if a < b + c else 2
    return answer
