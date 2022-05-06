# 줄 입력
n= int(input())
a=0

# 줄 만큼 반복문 수행
for i in range(n):
    # a만큼 공백 출력
    for _ in range(a):
        print(end=" ")
    # n만큼 *출력
    for j in range(n):
        print("*",end="")
    a+=1
    n-=1
    print()