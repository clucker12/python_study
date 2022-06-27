# 암호담을 리스트 n 선언
n = []
# while문 실행
while(True):
    # 암호 입력
    n.append(list(map(str, input())))
    # END가 나오면 while문 종료
    if("".join(n[-1]) == 'END'):
        break

# 리스트 마지막 인덱스 빼고 반복문 실행
for i in n[:-1]:
    # 거꾸로 출력
    print("".join(i[::-1]), end="")
    print()
