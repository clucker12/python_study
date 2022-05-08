import sys

# 학기수 입력
T = int(sys.stdin.readline())

# 학기수 만큼 반복수행
for i in range(T):
    # 과목수 입력
    n=int(sys.stdin.readline())
    total_c=0
    gpa=0
    # 과목수만큼 반복수행
    for j in range(n):
        # 학점과 성적 입력
        c,g=sys.stdin.readline().split()
        total_c+=int(c)
        gpa+=float(g)*int(c)
    print(total_c,'%.1f' %(gpa/total_c))

# # 다른사람 풀이
# T = int(input())

# for _ in range(T):
#     N = int(input())
#     total_credit = 0
#     total_grade = 0
    
#     for _ in range(N):
#         credit, grade = map(float, input().split())
#         total_credit += credit
#         total_grade += credit * grade
        
#     GPA = total_grade / total_credit
#     print(int(total_credit), '%.1f' % GPA)

# 주의점
# 평점 구하는 공식은 총(성적*학점)/총 학점