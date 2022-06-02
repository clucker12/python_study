import sys

# 몇개줄인지 입력 받음
n = int(sys.stdin.readline())

# n만큼 반복수행
for i in range(n):
    # 문자를 입력 받음
    a = list(map(str, input()))
    # 첫글자가 소문자면 대문자로 바꿔줌
    if(ord(a[0]) >= 97 and ord(a[0]) <= 122):
        a[0] = chr(ord(a[0])-32)
    # 첫글자를 대문자로 바꾼뒤 출력
    for j in a:
        print(j, end="")
    print()

# # 다른사람 풀이 upper() 사용
# # 몇개줄인지 입력 받음
# n = int(input())
# # n만큼 반복수행
# for i in range(n):
#     # 문자를 입력 받음
#     a = list(input())
#     # 소문자를 대문자를 바꿔준다
#     a[0] = a[0].upper()
#     # join을 이용하여 리스트를 문자열로 출력
#     print(''.join(a))
