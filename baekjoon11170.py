import sys

# 테스트 케이스수 입력
t = int(sys.stdin.readline())

# 테스트 수만큼 반복수행
for i in range(t):
    # n,m입력
    n, m = map(int, sys.stdin.readline().split())
    # 0개수 변수선언
    count_o = 0
    # n,m까지 반복
    for j in range(n, m+1):
        # 0의개수 구해 count_o에 저장
        count_o += str(j).count('0')
    print(count_o)
