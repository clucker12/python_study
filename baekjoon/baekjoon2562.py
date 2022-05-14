import sys

# 배열 선언
a = [0]

# 9번 반복수행
for i in range(9):
    # 자연수를 입력하고 a배열에 추가
    n = int(sys.stdin.readline())
    a.append(n)
# a배열에서 최댓값을 구함
print(max(a))
# 최댓값이 몇번째 인덱스인지 구함
print(a.index(max(a)))
