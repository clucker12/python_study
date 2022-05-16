import sys

a = []

for i in range(7):
    n = int(sys.stdin.readline())
    if(n % 2 == 1):
        a.append(n)
if(len(a) != 0):
    print(sum(a))
    print(min(a))
else:
    print(-1)
