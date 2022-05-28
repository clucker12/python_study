import sys

# 테스트케이스 개수 입력
t = int(sys.stdin.readline())

# t만큼 반복수행
for i in range(t):
    # 점수 입력받을 리스트 선언
    n = []
    # 점수입력
    n = list(map(int, sys.stdin.readline().split()))
    # 최대값 제거
    n.remove(max(n))
    # 최소값 제거
    n.remove(min(n))
    # 3명의 점수중 최대값 -최소값이 4보다
    # 작으면 총점 출력
    if(max(n)-min(n) < 4):
        print(sum(n))
    # 아닌경우 kin출력
    else:
        print('KIN')
