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


def solution(n):
    answer = sorted(list(set(primefactor(n))))
    return answer


# 틀렸던 부분
# set 함수를 사용한 후 배열로 선언하면 집합에서 어떤 원소를 먼저 출력할지 모르기 때문에
# sorted 함수를 사용하여 정렬해줘야 한다!!

# Test the solution function for numbers from 2 to 10000
for n in range(2, 10001):
    try:
        solution(n)
    except Exception as e:
        print(f"Error for n={n}: {e}")
