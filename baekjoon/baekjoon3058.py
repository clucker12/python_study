import sys

# 테스트개수 입력
t = int(sys.stdin.readline())

# 테스트 수만큼 반복수행
for i in range(t):
    # 자연수 7개 입력
    n = list(map(int, sys.stdin.readline().split()))
    # 짝수담을 리스트 선언
    jja = []
    # n리스트 개수만큼 반복수행
    for j in range(len(n)):
        # n[j]값이 짝수면 짝수리스트에 담기
        if(n[j] % 2 == 0):
            jja.append(n[j])
    # 짝수의 합과 최솟값을 출력
    print(sum(jja), min(jja))
