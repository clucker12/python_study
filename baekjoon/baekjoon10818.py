import sys

#  주어진 정수 n개 입력
n = int(sys.stdin.readline())
# n만큼 정수 입력
m = list(map(int, sys.stdin.readline().split()))
# 최대값 출력
print(min(m), end=" ")
# 최솟값 출력
print(max(m))
