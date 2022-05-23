from posixpath import split
import sys

# 정수의 개수 입력
n = int(sys.stdin.readline())
# 정수개만큼 입력
a = list(map(int, sys.stdin.readline().split()))
# 찾으려고 하는 정수 입력
v = int(sys.stdin.readline())
count_a = 0
# n만큼 반복수행
for i in range(n):
    # 찾으려고 하는 정수v가 있으면 count_a 1증가
    if(a[i] == v):
        count_a += 1
print(count_a)
