# # ord는 문자를 아스키코드 값을 바꾸는 내장함수
# a=ord(input())
# print(a)

# # chr은 10진수를 유니코드문자로 변환시키는 함수
# a=int(input())
# print(chr(a))

# # codeup 100제 6033
# n=ord(input())
# print(chr(n+1))

# # 6034 list map함수 사용 예시
# a,b=list(map(int,input().split()))
# print(a-b)

# # 6035
# a,b=list(map(float,input().split()))
# print(a*b)

# # 6036
# a,b=input().split()
# b=int(b)
# print(a*b)

# # 6037
# a=int(input())
# b=input()
# print(b*a)

# # 6038 **제곱의 연산자
# a,b=list(map(int,input().split()))
# print(a**b)

# # 6039
# a,b=list(map(float,input().split()))
# print(a**b)

# # 6040 //몫계산 연산자
# a,b=list(map(int,input().split()))
# print(a//b)

# # 6042
# a=float(input())
# print("{:.2f}".format(a))

# # 6043
# a,b=list(map(float,input().split()))
# print("{:.3f}".format(a/b))

# # 6044
# a,b=list(map(int,input().split()))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(format(a/b,".2f"))

# # 6045
# a,b,c=list(map(int,input().split()))
# sum=a+b+c
# avg=sum/3
# print("{} {:.2f}".format(sum,avg))

# # 6047 <<:2배곱 >>:1/2
# a,b=list(map(int,input().split()))
# print(a<<b)

# # 6048 a가 B보다 작은경우 True 아니면 false로 출력이 된다
# a,b=list(map(int,input().split()))
# print(a<b)
 
# # 6064 삼항 연산자 (변수 if(조건식) else 변수)
# a,b,c=list(map(int,input().split()))
# d=(a if(a<b) else b)
# e=(d if(d<c) else c)
# print(e)

# a,b,c=list(map(int,input().split()))
# if(a%2==0):
#     print(a)
# if(b%2==0):
#     print(b)
# if(c%2==0):
#     print(c)

# # 6082
# n=int(input())
# for i in range(1,n+1):
#     if(i%10==3 or i%10==6 or i%10==9):
#         print("X",end=" ")
#     else:
#         print(i,end=" ")

# # 72번
# a=int(input())
# while a!=0:
#     print(a)
#     a= a-1

# # 73번
# a=int(input())
# while (a-1>=0):
#     a=a-1
#     print(a)


# # 74번
# n=ord(input())
# i=ord('a')
# while n>=i:
#     print(chr(i),end =" ")
#     i+=1

# # 75번
# i=int(input())
# j=0
# while i>=j:
#     print(j)
#     j+=1

# # 76번
# n=int(input())
# for i in range(n+1):
#     print(i)

# # 77번
# a=int(input())
# sum=0
# for i in range(1,a+1):
#     if(i%2==0):
#         sum+=i
# print(sum)

# # 78번
# while True:
#     a=input()
#     print(a)
#     if(ord(a)==113):
#         break

# # 79번
# a=int(input())
# sum=0
# for i in range(1001):
#     sum+=i
#     if(a<=sum):
#         break
# print(i)

# # 80번
# n,m=list(map(int,input().split()))
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(i,j)

# # 81번 진짜 어려웠음
# # Tip
# # 문자열 인덱싱을 사용해서 [2:]쓴다(hex(i)는 문자열이기 때문에 사용가능)
# # 16진수 변환 함수 hex()를 이용해보자.
# # 소문자를 대문자로 변환하는 함수는 문자열의 메소드 중 upper()가 있다.
# a=input()
# for i in range(1,16):
#     print("{}*{}={}".format(a,hex(i)[2:].upper(),hex(int(a,16)*i)[2:].upper()))

# # 83번
# r,g,b=list(map(int,input().split()))
# count=0
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i,j,k)
#             count+=1
# print(count)

# # 84번
# h,b,c,s=list(map(int,input().split()))
# m_data=h*b*c*s
# mb_byte=m_data/(8*1024**2)
# print('{:0.1f} MB'.format(mb_byte))

# # 85번
# w,h,b=list(map(int,input().split()))
# bit_a=w*h*b
# mb_a=bit_a/(8*1024**2)
# print('{:0.2f} MB'.format(mb_a))

# # 86번
# a=int(input())
# sum=0
# i=1
# while True:
#     sum+=i
#     i+=1
#     if(sum>=a):
#         break
# print(sum)

# # 87번
# a=int(input())
# for i in range(a+1):
#     if(i%3!=0):
#         print(i,end=" ")

# # 88번
# a,d,n=list(map(int,input().split()))
# for i in range(1,n):
#     a+=d
# print(a)

# # 89번
# a,r,n=list(map(int,input().split()))
# for i in range(1,n):
#     a*=r
# print(a)

# # 90번
# a,m,d,n=list(map(int,input().split()))
# for i in range(1,n):
#     a=a*m+d
# print(a)

# # 91번 -1
# a,b,c=list(map(int,input().split()))
# day=0
# while True:
#     day+=1
#     if(day%a==0 and day%b==0 and day%c==0):
#         break
# print(day)

# 91번 -2
a,b,c=list(map(int,input().split()))
day=1
while day%a!=0 or day%b!=0 or day%c!=0:
    day+=1
print(day)