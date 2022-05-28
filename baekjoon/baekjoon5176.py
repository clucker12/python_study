import sys

# 테스트 케이스의 개수 입력
k = int(sys.stdin.readline())

# k만큼 반복수행
for i in range(k):
    # 리스트 a선언
    a = []
    # 참가자의 수와 자리의 수 입력
    p, m = map(int, sys.stdin.readline().split())
    # 참가자수만큼 반복수행
    for j in range(p):
        # a리스트에 1번부터 M번까지 수 입력
        a.append(int(sys.stdin.readline()))
    # 리스트에를 집합으로 만든다
    b = set(a)
    # 참가자수 - 집합의 개수는
    # 참가하지 못하는 사람수 출력
    print(p-len(b))
