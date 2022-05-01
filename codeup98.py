d=[[0 for i in range(11)]for j in range(11)]
for i in range(1,11):
    a=list(map(int,input().split()))
    for j in range(1,11):
        d[i][j]=a[j-1]
x=2
y=2
while x<=9 and y<=10:
    if(d[x][y]==0):
        d[x][y]=9
        y+=1
    elif(d[x][y]==1):
        y-=1
        x+=1
    elif(d[x][y]==2):
        d[x][y]=9
        break
for i in range(1,11):
    for j in range(1,11):
        print(d[i][j], end=' ')
    print()
# 주의점
# while문의 범위조건을 잘 정의해야함
# while문은 범위 조건식이 참인동안 계속 반복해서 수행