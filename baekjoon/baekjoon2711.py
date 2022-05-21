import sys

# 테스트 개수 입력
a = int(sys.stdin.readline())

# a만큼 반복수행
for i in range(a):
    # n은 오타를 낸 위치, m은 문자열 입력
    n, m = sys.stdin.readline().split()
    # 오타낸위치빼고 출력
    print(m[:int(n)-1]+m[int(n):])
