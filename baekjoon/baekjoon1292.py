import sys

# 수열 리스트 선언
n = [0]

# 시작과 끝 구간 입력
a, b = map(int, sys.stdin.readline().split())

# 수열 리스트 넣기
for i in range(b+1):
    for j in range(i):
        n.append(i)

# a부터 b까지 합 출력
print(sum(n[a:b+1]))
