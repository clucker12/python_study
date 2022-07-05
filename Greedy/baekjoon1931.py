import sys

# 회의의 수 입력
n = int(sys.stdin.readline())
# 회의의 시작과 끝나는 시간 담을 리스트 선언
a = []
# 시작과 끝나는시간 회의 수만큼 입력
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
a_count = 0
# 끝나는시간,시작하는 시간 순서로 오름차순 정렬
a.sort(key=lambda x: (x[1], x[0]))
# 시작시간 변수 선언
b = 0
for i in range(n):
    # 시작하는시간이 끝나는시간 보다 작으면 조건문 실행
    if(b <= a[i][0]):
        b = a[i][1]
        # 카운트수 증가
        a_count += 1
# 회의 최대 개수 출력
print(a_count)
