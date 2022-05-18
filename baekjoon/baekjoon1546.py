import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a_max = max(a)
sum = 0

for i in range(n):
    sum += (a[i]/a_max*100)
print("%f" % (sum/n))
