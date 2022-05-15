import sys
# 0번째 피보나치 수는 0이고,
# 1번째 피보나치 수는 1이다
n = [0, 1]

# n번째 피보나치 수입력
a = int(sys.stdin.readline())

# 1부터 a+1까지 반복수행
for i in range(1, a+1):
    # 피보나치수 이용
    sum = n[i-1]+n[i]
    # n배열에 추가
    n.append(sum)
# n번째 피보나치수 출력
print(n[a])
