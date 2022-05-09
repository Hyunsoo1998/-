N=int(input())

def recursive(N):
    if N==0:
        return 1
    if N==1:
        return 1
    return N*recursive(N-1)




recursive(N)
print(recursive(N))