import sys

# 테스트 케이스 개수
t = int(sys.stdin.readline())

for i in range(t):
    # 자연수 개수
    n = int(sys.stdin.readline())
    m = list(map(int, sys.stdin.readline().split()))
    print(sum(m))
