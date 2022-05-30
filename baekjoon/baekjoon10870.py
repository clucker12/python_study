import sys

# 자연수 n입력
n = int(sys.stdin.readline())

# 피보나치수 리스트 선언
a = [0, 1]

# n만큼 반복수행하여 a리스트에 피보나치수 추가
for i in range(n):
    a.append(a[i]+a[i+1])

# n번째 피보나치 수를 출력
print(a[n])
