import sys

# w 대학의 점수 담을 리스트 선언
w = []
# k 대학의 점수 담을 리스트 선언
k = []

# 20번 반복수행
for i in range(20):
    # 0~9까지는 w 대학 점수 입력
    if(i < 10):
        w.append(int(sys.stdin.readline()))
    # 10~19까지는 k 대학 점수 입력
    else:
        k.append(int(sys.stdin.readline()))
# 점수를 내림 차순 정렬
w.sort(reverse=True)
k.sort(reverse=True)
sum_w = 0
sum_k = 0

# 3번째로 점수가 높은 사람까지의 합 구하기
for i in range(3):
    sum_w += w[i]
    sum_k += k[i]
print(sum_w, sum_k)
