def primefactor(n):
    p = []
    N = n
    i = 2
    while N != 1:
        if N % i == 0:
            N = N / i
            p.append(i)
        else:
            i += 1
    return p


def solution(a, b):
    ap = primefactor(a)
    bp = primefactor(b)
    for n in ap:
        if n in bp:
            bp.remove(n)
    answer = 1 if set(bp) <= {2, 5} else 2
    return answer
