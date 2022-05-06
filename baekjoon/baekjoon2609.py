# a,b=list(map(int,input().split()))

# if(a<b):
#     c=b
# else:
#     c=a

# # 1부터 c값까지 반복문 진행
# for i in range(1,c+1):
#     if(a%i==0 and b %i==0): # a,b 둘다 나머지가 0인 순간이 최대 공약수
#         d=i

# # a,b 곱의 최대공약수를 나누면 최소공배수
# e=(a*b)//d

# print(d)
# print(e)

# # 유클리드 호제법
# a, b = map(int, input().split())

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return a * b // gcd(a, b)

# print(gcd(a, b))
# print(lcm(a, b))

# 함수 이용법
import math

a,b=map(int,input().split())

print(math.gcd(a,b))
print(math.lcm(a,b))



