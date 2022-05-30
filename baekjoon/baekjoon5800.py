import sys

# 테스트 개수 입력
t = int(sys.stdin.readline())

# 테스트 수만큼 반복수행
for i in range(t):
    # 학생수, 각 학생의 수학 성적 입력
    n = list(map(int, sys.stdin.readline().split()))
    # 수학성적을 내림차순으로 정렬
    n = sorted(n[1:], reverse=True)
    # 점수 차이 변수 선언
    gap = 0
    # 리스트 n의 개수 -1만큼 반복 수행
    for j in range(len(n)-1):
        # 점수 차이가 가장큰것을 구하는 조건문
        if(gap > n[j]-n[j+1]):
            gap = gap
        else:
            gap = n[j]-n[j+1]
    # 반 번호 출력
    print("Class %d" % (i+1))
    # 가장 높은 점수, 낮은 점수, 성적 출력
    print("Max %d, Min %d, Largest gap %d" % (max(n), min(n), gap))
