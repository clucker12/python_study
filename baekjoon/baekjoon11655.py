import sys

# 문자열 입력
n = list(map(str, input()))
# ROT13암호화한 내용 리스트 선언
m = []

# 문자열 만큼 반복
for i in n:
    # a~z이면 반복문실행
    if(65 <= ord(i) <= 90):
        if(65 <= ord(i)+13 <= 90):
            m.append(chr(ord(i)+13))
        else:
            m.append(chr(ord(i)-13))
    # A~Z이면 반복문 실행
    elif(97 <= ord(i) <= 122):
        if(97 <= ord(i)+13 <= 122):
            m.append(chr(ord(i)+13))
        else:
            m.append(chr(ord(i)-13))
    # 공백,숫자를 리스트에 추가
    else:
        m.append(i)
# n을 ROT13으로 암호화한 내용을 출력
print("".join(m))

# 조건식의 범위를 잘 계산 해야한다!!
