import sys

# 테스트개수 입력
t = int(sys.stdin.readline())

# 테스트 수만큼 반복 수행
for i in range(t):
    # 문자열 입력
    n = input()
    # 첫번째 글자 출력
    print(n[0], end="")
    # 마지막 글자 출력
    print(n[-1])
