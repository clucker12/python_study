import sys

# 10개의 자연수 넣을 배열 선언
a = []

# 1000보다 작은 배열에 0 넣어 선언
count_a = [0 for i in range(1001)]

# 자연수 10개 배열에 넣기
for i in range(10):
    a.append(int(sys.stdin.readline()))
sum_a = sum(a)

# a에 해당하는 수이면 count_a배열 +1
for j in a:
    count_a[j] += 1

# 평균값 출력
print(sum_a//10)

# 최빈값 출력
print(count_a.index(max(count_a)))
