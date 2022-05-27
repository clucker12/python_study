import sys

# 5개 숫자 넣을 리스트 선언
a = []

# 5번 반복수행
for i in range(5):
    # a리스트에 값 추가
    a.append(int(sys.stdin.readline()))
# a리스트를 오름차순 정렬
a.sort()
# 평균값 출력
print(sum(a)//5)
# 중앙값 출력
print(a[2])
