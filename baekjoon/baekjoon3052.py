import sys

# 리스트 선언
a = []

# 10개의 숫자 입력
for i in range(10):
    n = int(sys.stdin.readline())
    # 나머지값 a리스트에 넣기
    a.append(n % 42)
# b라는 집합 선언
b = set(a)
# 집합의 개수 출력
print(len(b))

# 주의점
# 집합선언은 set(집합할 대상)
