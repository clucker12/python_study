import sys
# sys.stdin.readline()으로 입력 값을 받음
n = int(sys.stdin.readline())

# a의 합 선언
sum_a = 0

# 멀티탭갯수(n)만큼 반복수행
for i in range(n):
    # 각 멀티탭의 플러그 갯수입력
    a = int(sys.stdin.readline())
    # 플러그 개수 합
    sum_a += a

# 플러그 개수 합에서 멀티탭 개수 -1 계산
sum_a -= (n-1)
print(sum_a)
