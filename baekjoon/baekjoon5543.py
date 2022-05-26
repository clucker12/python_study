import sys

# 햄버거 리스트 선언
a = []
# 음료수 리스트 선언
b = []

# 5번 반복수행
for i in range(5):
    # 2이하이면 햄버거 가격 입력해 배열에 추가
    if(i <= 2):
        a.append(int(sys.stdin.readline()))
    # 3이상이면 음료수 가격 입력해 배열에 추가
    else:
        b.append(int(sys.stdin.readline()))

# 가장 싼 세트 메뉴의 가격 출력
print(min(a)+min(b)-50)
