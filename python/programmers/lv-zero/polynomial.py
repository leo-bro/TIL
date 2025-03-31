def solution(polynomial):
    poly = polynomial.split(" + ")
    polyx = []
    for p in poly:
        if "x" in p:
            if p == "x":
                polyx.append("1x")
            else:
                polyx.append(p)
    coeff = sum([int(x[:-1]) for x in polyx])
    const = sum([int(p) for p in poly if not "x" in p])
    coeff = "" if coeff == 1 else coeff
    if (coeff == 0) & (const == 0):
        answer = "0"
    elif coeff == 0:
        answer = f"{const}"
    elif const == 0:
        answer = f"{coeff}x"
    else:
        answer = f"{coeff}x + {const}"
    return answer


print(solution("2x + 3x + 4"))  # 5x + 4
