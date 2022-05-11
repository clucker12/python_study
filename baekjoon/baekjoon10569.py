import sys

# 테스트 케이스의 수만큼 입력
T = int(sys.stdin.readline())

for i in range(T):
    # V : 꼭짓점의 수, E: 모서리의 수
    V, E = map(int, sys.stdin.readline().split())
    # 면의 수 = 모서리의수 - 꼭짓점의수 + 2
    a = E-V+2
    print(a)
