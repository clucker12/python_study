import sys
# 테스트 케이스의 개수 입력
n = int(sys.stdin.readline())

# n만큼 반복
for i in range(n):
    # 주사위 두번 던져 나온 값 입력
    a, b = map(int, sys.stdin.readline().split())
    # a+b로 두수의 합 출력
    print("Case %d: %d" % (i+1, a+b))
