import sys

# 테스트 수 입력
t = int(sys.stdin.readline())

# 테스트 수만큼 반복 수행
for i in range(t):
    # 길이가 같은 두 단어입력
    n = list(map(str, input().split()))
    print("Distances: ", end="")
    # 단어의 길이만큼 반복 수행
    for j in range(len(n[0])):
        # 알파벳 거리 변수 c 저장
        c = ord(n[1][j])-ord(n[0][j])
        # 알파벳 거리 차가 음수이면 c+26
        if(c < 0):
            print(c+26, end=" ")
        # 알파벳 거리 차가 음수가 아니면 c
        else:
            print(c, end=" ")
    print()

# 다른사람 풀이도 보기
