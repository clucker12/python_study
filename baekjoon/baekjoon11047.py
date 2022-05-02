n,k=map(int,input().split()) #n은 종류수, k는 돈의합
a=[]
count=0 # k원을 만드는데 필요한 동전의 개수의 최솟값
for i in range(n):
    a.append(int(input())) 

while True:
    count+=k//a[n-1]
    k=k%a[n-1]
    n-=1
    if(k==0):
        break
print(count)