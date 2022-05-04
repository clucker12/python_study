# 시간 문제는 초로 변환한 다음에 구하면 편하다!!

import sys

# 현재시간을 리스트로 입력
per_time=list(map(int,sys.stdin.readline().split(":")))

# 임무시작시간을 리스트로 입력
start_time=list(map(int,sys.stdin.readline().split(":")))

# 현재시간을 초로 변환
per=per_time[0] *3600 + per_time[1] * 60 + per_time[2]

# 임무시작시간을 초로 변환
start=start_time[0] *3600 + start_time[1] * 60 + start_time[2]

# 임무시작시간 - 현재시간을 구함
second=start - per

# 임무시작시간 - 현재시간이 마이너스면 24시간을 더함
if(second<0):
    second+= 24*60*60

# 60을 나누어 분으로 변환
minu=second//60
# 60나머지값으로 초를 구함
second %=60
# 60나누어 시간으로 변환
hour=minu//60
# 60나머지값으로 분을구함
minu%=60
# 24나머지값으로 시간을 구함
hour%=24

print("%02d:%02d:%02d" %(hour,minu,second))







