solution1 = lambda a, n: sorted(a, key=lambda x: (abs(x - n), x))
solution2 = lambda a, n: sorted(a, key=lambda x: (abs(x - n), x))[0]

print(solution1([5, 14, 28, 19, 29, 6, 8], 27))  # [28, 29, 19, 14, 6, 5, 8]
print(solution2([5, 14, 28, 19, 29, 6, 8], 27))  # 28

# 주어진 리스트 a에서 n과 가장 가까운 값을 찾는 함수
# 1. 리스트 a를 정렬하는데, 정렬 기준은 다음과 같다:
#    - 첫 번째 기준: 각 요소와 n의 차이의 절대값 (abs(x-n))
#    - 두 번째 기준: 첫 번째 기준이 동일한 경우, 요소 자체의 값 (x)
# 2. 정렬된 리스트의 첫 번째 요소를 반환
