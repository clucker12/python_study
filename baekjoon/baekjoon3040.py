import sys

# 모자에 쓰인 숫자를 담을 리스트 선언
n = []

# 9번 반복 수행
for i in range(9):
    # 모자에 쓰인 숫자 입력
    a = int(sys.stdin.readline())
    # n리스트에 숫자 추가
    n.append(a)

# n리스트의 합 -100하여 2명의 모자에 쓰인 합 변수선언
sum_n = sum(n)-100

# len(n)-1만큼 반복 수행
for i in range(len(n)-1):
    # i+1에서 len(n)만큼 반복수행
    for j in range(i+1, len(n)):
        # sum_n값이 n[i]+n[j]의 합과 값으면 조건문 수행
        if(sum_n == n[i]+n[j]):
            # b,c에 n[i],n[j]값 변수 선언
            b = n[i]
            c = n[j]
            # n리스트에 b,c값을 제거후 반복문 빠져나감
            n.remove(b)
            n.remove(c)
            break
    # n리스트 개수가 7이면 반복문 빠져나감
    if(len(n) == 7):
        break
# 리스트를 출력
for i in n:
    print(i)

# 런타임에러가 계속나서 너무 어렵다!!
# 다른사람 풀이를 다시 보면서 익혀야 겠다
