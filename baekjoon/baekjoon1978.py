import sys

n = int(sys.stdin.readline())
# 소수의 개수
count = 0
a = list(map(int, sys.stdin.readline().split()))
# n만큼 반복 수행
for i in range(n):
    # 약수의 개수
    b = 0
    # 1이면 다음 반복문실행
    if (a[i] == 1):
        continue
    # 2이면 소수개수증가하고 다음 반복문 실행
    elif (a[i] == 2):
        count += 1
        continue
    else:
        # 2부터 a[i]까지 반복수행
        for j in range(2, a[i]):
            # 나머지가 0인 경우가 있는경우 약수 개수 증가
            if(a[i] % j == 0):
                b += 1
        # 약수의 개수가 0인 경우 소수 이므로 소수 개수 증가
        if(b == 0):
            count += 1
print(count)

# # 다룬풀이 for else문
# # for문이 아닌경우 else문을 실행한다
# n = int(sys.stdin.readline())
# count = 0
# a = list(map(int, sys.stdin.readline().split()))
# for i in range(n):
#     if (a[i] == 1):
#         continue
#     elif (a[i] == 2):
#         count += 1
#         continue
#     else:
#         for j in range(2, a[i]):
#             if(a[i] % j == 0):
#                 break
#         else:
#             count += 1
# print(count)
