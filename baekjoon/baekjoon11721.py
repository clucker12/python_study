# 단어를 입력해 리스트로 만든다
n = list(map(str, input()))

# 출력할 개수를 a변수에 넣는다
if(len(n) % 10 == 0):
    a = len(n)//10
else:
    a = len(n)//10+1

# a만큼 반복수행
for i in range(a):
    # 10개씩 끊어서 한줄에 하나씩 출력
    print(''.join(n[10*i:10*i+10]))
