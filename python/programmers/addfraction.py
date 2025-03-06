def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    numer = numer // gcd(denom1, denom2)
    denom = denom // gcd(denom1, denom2)
    answer = [numer // gcd(numer, denom), denom // gcd(numer, denom)]

    return answer
