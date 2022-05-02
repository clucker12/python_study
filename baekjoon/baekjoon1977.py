import sys

# sys.sdin.readline으로 입력값 받음
M=int(sys.stdin.readline())
N=int(sys.stdin.readline())

# 배열 선언
a=[]

# 1~100까지 제곱수 구하기
for i in range(1,101):
    if(i**2>=M and i**2<=N):
        a.append(i**2)

# 리스트에 값이 없으면 -1, 있으면 리스트 합과 최솟값 출력
if(len(a)==0):
    print(-1)
else:
    print(sum(a))
    print(min(a))
