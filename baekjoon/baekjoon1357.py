import sys

# a,b를 문자열로 입력 받음
a, b = map(str, sys.stdin.readline().split())
# a,b를 역순으로 만들어준다
a = a[::-1]
b = b[::-1]
# 뒤집힌 a,b의 합을 구한다
sum_t = int(a)+int(b)
# 형변환을 이용하여 a,b의 합을 역순으로 만든다
print(int(str(sum_t)[::-1]))

# 다른사람풀이 다시보기
# 형변환을 주의해야함
