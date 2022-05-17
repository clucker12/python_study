import sys

# 날짜의 일의자리숫자
n = int(sys.stdin.readline())
# 자동차 번호의 일의 자리숫자
a = list(map(int, sys.stdin.readline().split()))
count = 0

# a만큼 반복수행
for i in a:
    # i가 n과 같으면 count증가
    if(i == n):
        count += 1
print(count)
