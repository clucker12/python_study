import sys

# 테스트 케이스 개수
t = int(sys.stdin.readline())

# t만큼 반복 수행
for i in range(t):
    # 방문할 상점의 수 입력
    n = int(sys.stdin.readline())
    # n만큼 상점의 위치 리스트에 넣기
    m = list(map(int, sys.stdin.readline().split()))
    # 모든 상점을 방문하고 차로 돌아오기 위해 걸어야 하는 거리의 최솟값 출력
    print((max(m)-min(m))*2)
