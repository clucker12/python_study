import sys

# 길이입력
n = int(sys.stdin.readline())
# a배열 입력
a = list(map(int, sys.stdin.readline().split()))
# b배열 입력
b = list(map(int, sys.stdin.readline().split()))
# 최소값구할 변수선언
s = 0
# n만큼 반복수행
for i in range(n):
    # a의 최대값 * b의 최솟값 합
    s += max(a)*min(b)
    # a의 최대값삭제
    a.remove(max(a))
    # b의 최솟값 삭제
    b.remove(min(b))
print(s)
