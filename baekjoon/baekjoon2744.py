# 주어진 단어 입력
n = list(map(str, input()))

# n리스트 개수만큼 반복수행
for i in range(len(n)):
    # a~z이면 A~Z로 변환하는 조건문
    if(n[i] >= chr(ord('a')) and n[i] <= chr(ord('z'))):
        n[i] = chr(ord(n[i])-32)
    # A~Z이면 a~z로 변환하는 조건문
    else:
        n[i] = chr(ord(n[i])+32)

for i in n:
    print(i, end="")

# 소문자와 대문자는 아스키코드로 32의 차이가 난다
