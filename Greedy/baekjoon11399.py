import sys

# 사람수 입력
n = int(sys.stdin.readline())
# 사람마다 걸리는 시간 입력
people = list(map(int, sys.stdin.readline().split()))
# 사람마다 걸린 시간
hap_1 = 0
# 사람마다 걸린 시간의 합
hap_2 = 0
for i in range(n):
    # 최솟값을 구해 걸린시간 구하기
    hap_1 += min(people)
    hap_2 += hap_1
    # 최소값을 제거
    people.remove(min(people))
print(hap_2)
