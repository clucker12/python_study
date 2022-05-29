import sys

# 돈을 부르는 수 입력
k = int(sys.stdin.readline())

# 부른 돈을 받을 리스트 선언
a = []

# k만큼 반복수행
for i in range(k):
    # 돈 입력
    b = int(sys.stdin.readline())
    # 부른 값이 0인경우 리스트 값 빼기
    if(b == 0):
        a.pop()
    # 아닌경우 a리스트에 b추가
    else:
        a.append(b)
# 적어 낸 수의 합 출력
print(sum(a))
