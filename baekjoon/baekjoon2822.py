# import sys
# # 점수 적을 리스트 선언
# n = [0]
# # 가장 높은 점수 5개받을 리스트 선언
# a = []
# # 가장 높은 점수 5개의 인덱스값을 받을 리스트 선언
# b = []
# # 가장 높은 점수 5개를 구할 변수 선언
# max_n = 0
# # 8개 점수 입력 받아 리스트에 넣기
# for i in range(8):
#     n.append(int(sys.stdin.readline()))

# # 가장 높은 점수 5개 구하는 반복문
# for i in range(5):
#     a.append(max(n))
#     b.append(n.index(max(n)))
#     n[n.index(max(n))] = 0
# # 가장 높은 점수 5개 합 출력
# print(sum(a))
# # 인덱스값 오름차순 정렬
# b.sort()
# # 인덱스값 출력
# for i in range(5):
#     print(b[i], end=" ")

# 다른 사람 풀이
# 점수와 인데스값을 리스트로 묶어 리스트 만듬
score = [[int(input()), i+1] for i in range(8)]
# 리스트를 x[0]을 기준으로 내림차순 정렬
score = sorted(score, key=lambda x: -x[0])
# 인데스 값만 넣어줄 리스트 선언
problem = []
# 점수합 구할 변수 선언
sum_score = 0

# 5개의 점수합과 인덱스 값을 구함
for i in range(5):
    sum_score += score[i][0]
    problem.append(score[i][1])
# 5개 점수합 출력
print(sum_score)
# 오름차순 정렬을 시킨 problem리스트를 반복수행
for i in sorted(problem):
    # 인덱스값 출력
    print(i, end=' ')
