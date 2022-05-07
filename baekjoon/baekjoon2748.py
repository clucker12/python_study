import sys

n=int(sys.stdin.readline())

# 피보나치 수는 0과 1로 시작한다. 
# 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다
sum=[0,1]

# 반복횟수는 n-1만큼 반복
for i in range(n-1):
    #  앞 두 피보나치 수의 합을 sum리스트에 넣는다
    sum.append(sum[i]+sum[i+1])

# n번째 피보나치 수 출력
print(sum[n])

# 주의점 
# 반복문 수행을 잘 생각해야한다