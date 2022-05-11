import sys

# 테스트 케이스의 수만큼 입력
n = int(sys.stdin.readline())

# 테스트 케이스의 수만큼 반복
for i in range(n):
    # 사탕의 개수c와 형제의 수v입력
    c, v = map(int, sys.stdin.readline().split())
    # 나눈 사탕의 수
    candy = c//v
    # 남은 사탕의 수
    candy_last = c % v
    print("You get %d piece(s) and your dad gets %d piece(s)." %
          (candy, candy_last))
