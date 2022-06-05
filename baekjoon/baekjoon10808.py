import sys

# 알파벳 개수 0으로 리스트 담기
n = [0 for i in range(26)]
# 알파벳 26개 리스트 담기
a = [chr(i) for i in range(97, 123)]

# 단어s를 리스트에 담기
s = list(map(str, input()))

# 단어s가 있으면 n리스트에 인덱스 +1증가
for i in s:
    for j in a:
        if(i == j):
            n[a.index(j)] += 1
            break

# 알파벳 개수 출력
for i in n:
    print(i, end=" ")

# 다른사람 풀이도 보기
