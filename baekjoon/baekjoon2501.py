import sys

n, k = map(int, sys.stdin.readline().split())

yak = []

for i in range(1, n+1):
    if(n % i == 0):
        yak.append(i)
# 약수의 개수가 k보다 크거나 같으면 출력
if(len(yak) >= k):
    print(yak[k-1])
# 약수의 개수가 k보다 작으면 0출력
else:
    print(0)
