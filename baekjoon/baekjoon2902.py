# -기준으로 나누어서 리스트에 넣기
n = list(map(str, input().split("-")))

# 리스트를 반복문 수행
for i in n:
    # 리스트의 0번인덱스를 출력
    print(i[0], end="")
