import sys

n = int(sys.stdin.readline())
sum = 1

# 1~n+1까지 반복문 수행
for i in range(1, n+1):
    sum *= i
print(sum)

# # 다른 풀이
# # 팩토리얼
# # 파이썬의 math 함수를 이용하여 팩토리얼 계산
# import math
# n = int(input())
# print(math.factorial(n))
