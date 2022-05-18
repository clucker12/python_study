import sys

# 문제수 입력
n = int(sys.stdin.readline())
# 채점결과를 0 혹은 1로 입력
a = list(map(int, sys.stdin.readline().split()))

jumsu = 0
count = 0

# 문제수만큼 반복수행
for i in range(n):
    # 1인경우 count 증가
    if(a[i] == 1):
        count += 1
    # 0인경우 count 0으로 초기화
    else:
        count = 0
    # 점수합을 count값 만큼 더하기
    jumsu += count
print(jumsu)
