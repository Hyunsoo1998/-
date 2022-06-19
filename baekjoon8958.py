import sys
N=int(sys.stdin.readline())



for j in range(N):
    count = 0
    hap = 0
    A = sys.stdin.readline().strip()
    for i in range(len(A)):
        if A[i]=='O':
            count+=1
            hap+=count
        elif A[i]=='X':
            count=0
    print(hap)


