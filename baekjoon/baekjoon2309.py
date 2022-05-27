from itertools import combinations
import sys

# 키입력받을 리스트 선언
a = []

# 9개 리스트 추가
for i in range(9):
    a.append(int(sys.stdin.readline()))

# 오름차순으로 정렬
a.sort()
# 100뺀값을 sum_a 변수에 선언
sum_a = sum(a)-100

# 8만큼 반복수행
for i in range(len(a)-1):
    # i+1부터 len(a)만큼 반복수행
    for j in range(i+1, len(a)):
        # sum_a == a[i]+a[j]이면
        # 리스트에 a[i],a[j]값 제거하고 빠져나감
        if(sum_a == a[i]+a[j]):
            a.remove(a[j])
            a.remove(a[i])
            break
    # len(a)가 7이면 빠져나감
    if len(a) == 7:
        break
# a리스트 출력
for i in a:
    print(i)

# # 다른사람풀이 함수이용
# # combinations(리스트,조합개수)

# arr = [int(input()) for _ in range(9)]

# # 리스트가 7인 조합으로 반복수행
# for i in combinations(arr, 7):
#     # 7개 조합의 합이 100인경우
#     # 오름차순 정렬로 출력후 빠져나옴
#     if sum(i) == 100:
#         for j in sorted(i):
#             print(j)
#         break
