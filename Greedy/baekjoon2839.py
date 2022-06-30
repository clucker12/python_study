import sys

n = int(sys.stdin.readline())
# 봉지 개수
count_n = 0
while(n > 0):
    # 5로 나눌때 나머지가 0인경우 if문 실행
    if(n % 5 == 0):
        count_n += (n//5)
        n -= (5*(n//5))
    else:
        # 나머지가 0이 아니고 n이 3보다 큰경우 if문 실행
        if(n >= 3):
            n -= 3
            count_n += 1
        # n이 3보다 작은경우 while문 탈출
        else:
            break
# n이 0이면 봉지 개수 출력
if(n == 0):
    print(count_n)
# 아닌경우 -1출력
else:
    print(-1)
