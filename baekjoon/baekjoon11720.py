import sys

# 숫자의 개수 입력
n = int(sys.stdin.readline())

# 숫자입력
a = sys.stdin.readline()
# 합변수 선언
sum_a = 0
# 숫자의 개수만큼 반복수행
for i in range(n):
    # 주어진 숫자 N개의 합구하기
    sum_a += int(a[i])
# 주어진 숫자 N개의 합출력
print(sum_a)
