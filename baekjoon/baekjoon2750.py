import sys

# 몇개의 수 주어질지 입력
n = int(sys.stdin.readline())
# a리스트 선언
a = []

# n만큼 반복수행
for i in range(n):
    # a리스트에 n개만큼의 수 넣기
    a.append(int(sys.stdin.readline()))

# 리스트를 오름차순 정렬
a.sort()

#  n개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력
for i in range(n):
    print(a[i])
