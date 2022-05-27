# 수 n입력
a = input()
# n을 담을 리스트 선언
b = []

# a개수 만큼 반복수행
for i in range(len(a)):
    # b리스트에 a[i]값 추가
    b.append(a[i])

# 내림차순 정렬된 리스트 반복수행
for i in sorted(b, reverse=True):
    # 내림차순으로 정렬한 수 출력
    print(i, end="")

# # # 다른 사람 풀이
# # 정렬하려고 하는 수 리스트로 만들기
# a = list(map(int, input()))
# # 내림차순으로 정렬
# a.sort(reverse=True)
# # 리스트 출력
# for i in a:
#     print(i, end="")
