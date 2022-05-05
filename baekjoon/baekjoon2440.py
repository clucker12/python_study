# 줄 입력
n=int(input())

# 줄 만큼 반복문 수행
for i in range(n):
    for j in range(n):
        print("*",end="")
    n-=1 # 수행 할때마다 별의 갯수 감소
    print("") 