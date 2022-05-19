import sys

# 탄사람 수 합 배열 선언
hap = []
# 합의 값 변수 선언
s = 0
# 4번 반복수행
for i in range(4):
    # 역마다 내린사람,탄사람수 배열 초기화
    a = []
    # 역마다 내린사람,탄사람수 배열에 대입
    a = list(map(int, sys.stdin.readline().split()))
    # 역마다 탄 사람수 합 구하기
    s += (a[1] - a[0])
    # 역마다 탄 사람수 합 배열에 넣기
    hap.append(s)
# 역마다 탄 사람수 합 최대값 구하기
print(max(hap))
