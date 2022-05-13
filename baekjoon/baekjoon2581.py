import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
# 소수값을 담을 빈 리스트 생성
sosu = []

# m에서 n+1만큼 반복수행
for i in range(m, n+1):
    # 1이면 다음 반복문실행
    if(i == 1):
        continue
    # 2이면 값을 리스트에 넣고 다음 반복문 실행
    elif(i == 2):
        sosu.append(i)
        continue
    else:
        # 2부터 i까지 반복수행
        for j in range(2, i):
            # 나머지가 0인 경우가 있는경우 반복문을 빠져 나옴
            if(i % j == 0):
                break
        # for문의 break분기문이 아닌경우 리스트에 값을 넣는다
        else:
            sosu.append(i)
# sosu리스트의 인덱스 개수가 0이 아닌 경우 합과 최솟값을 출력
if(len(sosu) != 0):
    print(sum(sosu))
    print(min(sosu))
# sosu리스트의 인덱스 개수가 0인 경우 -1출력
else:
    print(-1)
