import sys

# 테스트 개수 입력
t = int(sys.stdin.readline())

# 테스트 수만큼 반복수행
for i in range(t):
    # ,기준으로 나눠서 a,b의 수를 받음
    a, b = map(int, sys.stdin.readline().split(","))
    # a,b합 출력
    print(a+b)
