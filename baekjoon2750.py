
import sys
N=int(input())
a=[int(sys.stdin.readline()) for i in range(N)]
a.sort()

[print(a[i]) for i in range(N)]

