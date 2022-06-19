import sys

N=int(sys.stdin.readline())

A=[]
for i in range (N):
    A.append(int(sys.stdin.readline()))
A.sort()

for i in range(len(A)):
    print(A[i])


