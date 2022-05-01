# # 92번
# n=int(input()) #횟수
# a=list(map(int,input().split())) #부른 번호
# count=[]
# for i in range(24):
#     count.append(0)
# for i in range(n):
#     count[a[i]]+=1
# for i in range(1,24):
#     print(count[i],end=" ")

# # 93번
# n=int(input()) #횟수
# a=list(map(int,input().split())) #부른 번호
# for i in range(n-1,-1,-1):
#     print(a[i],end=" ")

# # 94번 -1
# n=int(input()) #횟수
# a=list(map(int,input().split())) #부른 번호
# anw=n
# for i in range(n):
#     if(anw>=a[i]):
#         anw=a[i]

# print(anw)

# 94번 -2 min()함수: 배열객체의 원소중 가장 작은 값을 반환하는 함수
n=int(input()) #횟수
a=list(map(int,input().split())) #부른 번호
print(min(a))