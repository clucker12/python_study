import sys

n=int(sys.stdin.readline())

last_ap=0

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    last_ap+=(b%a)
print(last_ap)