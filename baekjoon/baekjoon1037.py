import sys

# n의 진짜 약수의 개수 입력
n = int(sys.stdin.readline())
# n의 진짜 약수의 개수만큼 약수 입력
m = list(map(int, sys.stdin.readline().split()))

# 약수중에 최소값
m_min = min(m)
# 약수중에 최대값
m_max = max(m)
# 최소값과 최대값의 곱은 해당 양수
print(m_max*m_min)
