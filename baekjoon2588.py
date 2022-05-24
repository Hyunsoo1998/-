A=int(input())
B=int(input())
array=[0,0,0]
array[2]=B%10
array[1]=(B%100)//10
array[0]=B//100

print(A*array[2])
print(A*(array[1]))
print(A*array[0])

print((A*array[0]*100)+((A*array[1]*10))+(A*array[2]))