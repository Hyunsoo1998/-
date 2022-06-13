#단위: BMI(체중kg/신장m2)

#140.1 미만은 체중과 상관없이 6급
#140.1이상 146미만은 체중과 관계없이 5급
#146 이상 159 미만 4급

import sys

N=int(input())
BMI=0
for i in range(N) :
    cm,kg=map(int,sys.stdin.readline().split())
    BMI=(kg/((cm*0.01)*(cm*0.01)))
    if cm <140.1:
        print(6)
    elif 140.1<=cm and cm<146:
        print(5)
    elif 146<= cm and  cm<159:
        print(4)

    if 159<=cm and cm<161:
        if BMI>=16 and BMI<35:
            print(3)
        elif BMI<16 or BMI>=35:
            print(4)
    if cm>=161 and cm<204:
        if BMI>=20 and BMI<25:
            print(1)
        elif BMI>=18.5 and BMI<20:
            print(2)
        elif BMI>=25 and BMI<30:
            print(2)
        elif BMI>=16 and BMI<18.5:
            print(3)
        elif BMI>=30 and BMI<35:
            print(3)
        elif BMI<16 or BMI>=35:
            print(4)
    if cm>=204:
        print(4)
