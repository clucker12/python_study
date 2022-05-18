import sys

# 시험본 과목의 개수
n = int(sys.stdin.readline())
# 현재 성적 입력
a = list(map(int, sys.stdin.readline().split()))
# 성적에서 최대값
a_max = max(a)
sum = 0

# 과목수만큼 반복수행
for i in range(n):
    # 자기점수/자기점수최대값*100의 합
    sum += (a[i]/a_max*100)
print("%f" % (sum/n))
