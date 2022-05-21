import sys

# 배열 선언
a = [0]

# 5참가자 점수 입력
for i in range(5):
    n = list(map(int, sys.stdin.readline().split()))
    # 점수합 배열에 넣기
    a.append(sum(n))

# 우승자 번호 출력
print(a.index(max(a)), end=" ")
# 우승자 점수 출력
print(max(a))
