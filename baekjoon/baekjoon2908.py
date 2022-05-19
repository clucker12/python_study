import sys

# 두수를 입력
a, b = map(int, sys.stdin.readline().split())
# a를 반대로 바꾸기
a = a % 10*100+(a//10) % 10*10+(a//100)
# b를 반대로 바꾸기
b = b % 10*100+(b//10) % 10*10+(b//100)

# 큰수 출력하기
if(a > b):
    print(a)
else:
    print(b)

# # 다른 사람 풀이
# print(max(map(int, input()[::-1].split())))
# # [::1]
# # 문자열을 거꾸로 뒤집는다
