import sys

# 숫자 세 개 입력
n = list(map(int, sys.stdin.readline().split()))

# 제일 작은 수, 그 다음 수, 제일 큰 수를 차례대로 출력
for i in sorted(n):
    print(i, end=" ")
