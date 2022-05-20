import sys

sum_a = 1

# 세개의 자연수의 곱을 구함
for i in range(3):
    a = int(sys.stdin.readline())
    sum_a *= a

# 0~9까지 각각의 숫자가 몇 번씩 쓰였는지 구함
for j in range(10):
    print(str(sum_a).count(str(j)))

# 주의점
# 형변환을 주의해야함
