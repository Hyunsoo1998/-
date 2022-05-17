import sys
N,X=map(int,sys.stdin.readline().split())

for i in range(N):
    A=map(int,sys.stdin.readline().split())
    if A<i:
        print(A)



