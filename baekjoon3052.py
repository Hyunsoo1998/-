#변수명.append를 이용해서 리스트에 넣어준다(끝에)
#set(): 저장된 자료형의 중복을 제거하기위해 set 함수를 이용한다
#set함수의 특징:
#중복을 허용하지 않는다 .  / 순서가 없다.
n=[]
for i in range(10):
    A=int(input())
    B=A%42
    n.append(B)
s=set(n)
print(len(s))



