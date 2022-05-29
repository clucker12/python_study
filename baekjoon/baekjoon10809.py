# 알파벳 26개 리스트 담기
n = []
for i in range(ord('a'), ord('z')+1):
    n.append(chr(i))

# 단언s입력 받아 리스트에 담기
s = list(map(str, input()))
# -1로 26개 리스트 담기
m = [-1 for i in range(26)]
# 단어s가 있으면 m리스트에 s리스트 인덱스 넣기
for i in s:
    for j in n:
        if(i == j):
            m[n.index(j)] = s.index(i)

for i in m:
    print(i, end=" ")
