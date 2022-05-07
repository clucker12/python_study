import sys

# 10권의 총가격입력
total_price=int(sys.stdin.readline())

# 2~10번 째줄 책 가격 입력
for i in range(9):
    total_price-=int(sys.stdin.readline())

# 1번째줄 책가격 출력
print(total_price)