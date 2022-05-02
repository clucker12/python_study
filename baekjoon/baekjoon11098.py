from random import randrange
import sys

# n은 테스트 케이스 횟수 입력
n=int(sys.stdin.readline())
maxplayer=[] # 가장 비싼 선수 배열 선언

# 테스트 케이스 n번 반복
for i in range(n):
    p=int(sys.stdin.readline()) # p는 n번째 케이스의 선수들의 수 입력
    cost=[] # 선수 가격 배열 선언
    player=[] # 선수이름 배열 선언
    for j in range(p): #p명의 선수 만큼 반복
        c,name=sys.stdin.readline().split() #p명의 선수 만큼 c,name 입력
        cost.append(int(c)) # 선수 가격 배열에 c추가
        player.append(name) # 선수이름 배열에 name 추가
    maxcost=cost.index(max(cost)) # 가장 비싼가격의 인덱스값 정의
    maxplayer.append(player[maxcost]) # 가장 비싼선수 배열에 player[maxcost]추가

for i in range(n): # 테스트 케이스 n번 반복
    print(maxplayer[i]) #테스트 케이스별 비싼 선수 출력