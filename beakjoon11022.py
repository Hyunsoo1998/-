import sys
N=int(input())

for x in range(1,N+1):
    A,B=map(int,sys.stdin.readline().split())
    C=A+B
    print("Case #{}: {} + {} = {}".format(x,A,B,C))

