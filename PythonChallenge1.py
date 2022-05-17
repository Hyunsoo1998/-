#과제1. 계산기 만들기
def plus(a,b):
    return a+int(b)

def minus(a,b):

    return a-b
def multiply(a,b):
    return int(a)*int(b)

def remainder(a,b):
    return a%b

def division(a,b):
    return a/b

def negation(a):
    return int(-a)

def double_multiply(a,b):
    return int(a)**b


print(plus(3,"5"))
print(minus(3,5))
print(multiply('3','5'))
print(remainder(5,4))
print(division(5,2))
print(negation(4))
print(multiply("5",2))


