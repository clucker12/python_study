import sys

# 테스트 수 입력
t = int(sys.stdin.readline())

# 테스트 수 만큼 반복
for i in range(t):
    # 10진수 값 이력
    n = int(sys.stdin.readline())
    # 2진수 변환
    n = bin(n)[2:][::-1]
    # 2진수 개수만큼 반복
    for j in range(len(n)):
        # n[j] == '1'이면 j값 출력
        if(n[j] == '1'):
            print(j, end=" ")

# 주의점
# 2진수 변환 할떄 0b로 시작하므로 [2::]이용해야
# 2진수값이 나오고 [::-1]해야 변환이 완료됨
