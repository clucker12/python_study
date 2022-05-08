# # 처음 푼 방식 출력 형식 오류 발생
# n=int(input())
# for i in range(n,0,-1):
#     print(" "*(n-5)+"*"*(2*i-1))
#     n+=1

# 다시 푼 정답 방식
n=int(input())

for i in range(n,0,-1):
    print(" "*(n - i)+"*"*(2*i-1))

# 오류가 나는 코드와 오류가 안나는 코드의
# 차이점을 모르겠다...