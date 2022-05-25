import sys
max=-100000
min=1000000
count =0
A=[0 for _ in range(9)]
for i in range(9):
    A[i]=int(input())
    if A[i]>max:
        max=A[i]
        count=i+1
print(max)
print(count)