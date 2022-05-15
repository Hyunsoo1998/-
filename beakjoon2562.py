
MAX=-100000
cnt=0
A=[]
for i in range(9):
    A.append(int(input()))
    if A[i]>MAX:
        MAX=A[i]
        cnt=i+1
print(A[cnt-1])
print(cnt)