#  문자열을 대문자로 저장
s = input().upper()
# 문자열 s를 집합처리하여 리스트에 저장
a = list(set(s))
# 리스트 선언
b = []

# a리스트 만큼 반복수행
for i in a:
    # b리스트에 s문자열에서 i인것의 개수를 추가
    b.append(s.count(i))

# b리스트에서 b의 최대값이 1개보다 많으면 ?출력
if b.count(max(b)) > 1:
    print("?")
# b리스트에서 b의 최대값이 1이하이면
# 가장 많이 사용된 알파벳을 대문자로 출력
else:
    print(a[b.index(max(b))])

# 많이 어려운 것 같다..
# set함수를 활용해서 하는 방법을 생각해야함
# 나중에 다시한번 풀어보기
