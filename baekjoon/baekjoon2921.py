import sys
# 도미노 세트의 크기N입력 N은 칸하나에 점의 수
n = int(sys.stdin.readline())

sum = 0
# 1부터 n+1까지 반복
for i in range(1, n+1):
    # i+1까지 반복
    for j in range(i+1):
        sum += (i+j)
print(sum)

# 주의점
# 규칙을 보면
# 1일때는 1+2
# 2일때는 2+3+4
# 3일때는 3+4+5+6
# 반복수가 1씩증가하고 더하는수도 1씩 증가하는
# 알고리즘을 알수있다
