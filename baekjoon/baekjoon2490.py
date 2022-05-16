import sys

for i in range(3):
    # 네 개의 정수(0 또는 1)을 입력
    n = list(map(int, sys.stdin.readline().split()))
    # 0의 개수에 따라
    # 도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력
    if(n.count(0) == 1):
        print('A')
    elif(n.count(0) == 2):
        print('B')
    elif(n.count(0) == 3):
        print('C')
    elif(n.count(0) == 4):
        print('D')
    else:
        print('E')
