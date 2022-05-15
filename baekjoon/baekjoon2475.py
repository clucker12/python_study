# import sys

# n = list(map(int, sys.stdin.readline().split()))

# # 배열 0~4까지 수를 제곱해서 더한값을 저장
# a = n[0]**2+n[1]**2+n[2]**2+n[3]**2+n[4]**2
# # 10으로 나눈 나머지 값 출력
# print(a % 10)

# 다른풀이
# for문을 활용
import sys

n = list(map(int, sys.stdin.readline().split()))
a = 0

for i in n:
    a += (i**2)
print(a % 10)
