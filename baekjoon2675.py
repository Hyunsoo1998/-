# import sys
# T=int(input())
#
# for i in range(T):
#     S, R = sys.stdin.readline().split()
#     R = list(R)
#     S = int(S)
#     for j in range(len(R)):
#         print(R[j]*S,end='')
#
#

T = int(input())


for _ in range(T):
    R, S = list(map(str, input().split()))
    R = int(R)

    for i in S:
        print(R*i, end='')
    print()