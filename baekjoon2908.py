import sys

A,B=map(int,input().split())

new_A=0
new_A+=(A%10)*100
new_A+=((A%100)//10)*10
new_A+=A//100

new_B=0
new_B+=(B%10)*100
new_B+=((B%100)//10)*10
new_B+=B//100
if new_B>new_A:
    print(new_B)
elif new_A>new_B:
    print(new_A)



