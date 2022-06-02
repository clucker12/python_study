# 단어를 입력해서 리스로 받음
n = list(map(str, input()))

# 모음 개수를 카운트할 변수 선언
count_n = 0

# 리스트n을 반복수행하여 모음이면 카운트증가
for i in n:
    if(i == 'a'):
        count_n += 1
    elif(i == 'e'):
        count_n += 1
    elif(i == 'i'):
        count_n += 1
    elif(i == 'o'):
        count_n += 1
    elif(i == 'u'):
        count_n += 1
# 모음의 개수 출력
print(count_n)
