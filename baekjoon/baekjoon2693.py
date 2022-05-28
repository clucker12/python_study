import sys

# 테스트케이스 수 입력
t = int(sys.stdin.readline())

# t만큼 반복수행
for i in range(t):
    # 10개의 값을 a리스트에 추가
    a = list(map(int, sys.stdin.readline().split()))
    # 내림차순으로 정렬
    a = sorted(a, reverse=True)
    # 3번째 큰 값을 출력
    print(a[2])
