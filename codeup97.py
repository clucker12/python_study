b,c=map(int,input().split())
a=[[0 for i in range(c+1)] for j in range(b+1)]
n=int(input())
for i in range(n):
    l,d,x,y=map(int,input().split())
    for j in range(l):
        if d==0:
            a[x][y]=1
            y+=1
        else:
            a[x][y]=1
            x+=1
for i in range(1,b+1):
    for j in range(1,c+1):
        print(a[i][j], end=' ')
    print()
# 주의점
# 배열을 만들때 b,c의 값 위치를 주의하기