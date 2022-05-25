import sys
N=int,sys.stdin.readline()
A=list(map(int,sys.stdin.readline().split()))
MAX=-1000001
MIN=1000001
for i in range(len(A)):
    if A[i]>MAX:
        MAX=A[i]
    if A[i]<MIN:
        MIN=A[i]

print(MIN,MAX)
