import sys
N=int(input())
for i in range(1,N+1):
    A,B=map(int,sys.stdin.readline().split())
    print("Case #{}:".format(i),A+B)
