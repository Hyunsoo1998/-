import sys

M=int(sys.stdin.readline())
N=int(sys.stdin.readline())
A=[]

for i in range(M,N+1):
    if i==1:
        pass
    elif i==2:
        A.append(i)
    else:
        for j in range(2, i):
            if i%j==0:
                break
            elif j==i-1:
                A.append(i)
if len(A)==0:
    print(-1)
else:
    print(sum(list(A)))
    print(min(list(A)))

