import sys

# 테스트 갯수 입력
a = int(sys.stdin.readline())
total_q = []

# a만큼 반복수행
for i in range(a):
    # 자동차 가격 입력
    s = int(sys.stdin.readline())
    # 옵션 개수 입력
    n = int(sys.stdin.readline())
    # 옵션가격입력
    price_t = 0
    # 옵션수 만큼 반복수행
    for j in range(n):
        # 특정 옵션의 개수q,옵션의 가격p입력
        q, p = map(int, sys.stdin.readline().split())
        # 옵션 가격 계산
        price_t += p*q
    # 자동차 가격 + 옵션 가격 계산후 배열에 넣기
    total_q.append(s+price_t)
# 테스트 갯수만큼 반복수행 출력
for i in range(a):
    print(total_q[i])


# import sys

# a=int(sys.stdin.readline())
# total_q=[]
# for i in range(a):
#     s=int(sys.stdin.readline())
#     n=int(sys.stdin.readline())
#     price_t=0
#     for j in range(n):
#         q,p=map(int,sys.stdin.readline().split())
#         price_t+=p*q
#     print(s+price_t)
