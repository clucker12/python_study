import sys

# 사람수를 n명입력
n=int(sys.stdin.readline())

# 사람의 생일,이름정보 배열 생성
person=[]

# 사람수만큼 반복 수행
for i in range(n):
    # 사람의 이름,일,월,년 순으로 정보입력
    person.append(list(map(str,sys.stdin.readline().split()))) 

# sort라는 정렬 메소드를 이용하여 key값으로 
# lambda를 이용해 정렬 오름차순으로 정렬한다
person.sort(key = lambda x:(int(x[-1]),int(x[-2]),int(x[-3])))

# person이라는 배열에 나이가 가장적은사람 출력 
print(person[-1][0])

# person이라는 배열에 나이가 가장많은사람 출력 
print(person[0][0])