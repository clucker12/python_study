import sys

# 총점 선언
sum = 0

# 5회 반복 수행
for i in range(5):
    # 점수 입력
    a = int(sys.stdin.readline())
    # 점수합 계산
    sum += a
print(sum)
