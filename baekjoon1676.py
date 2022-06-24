import sys

# n! n입력
n = int(sys.stdin.readline())
fac_n = 1
# n!구하기
for i in range(1, n+1):
    fac_n *= i

# n!뒤로 뒤집기
a = str(fac_n)[::-1]
count_a = 0

# 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하기
for i in range(len(a)):
    if(a.count('0') != 0):
        if(a[i] == '0'):
            count_a += 1
        else:
            break
    else:
        break
print(count_a)
