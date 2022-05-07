import sys

# a=0,b=0일때까지 반복문 수행
while True:
    # a,b입력
    a,b=map(int,sys.stdin.readline().split())
    # a!=0이고 b!=0일때만 출력 a=0이고 b=0이면 반복문 탈출
    if(a!=0 and b!=0):
        print(a+b)
    else:
        break