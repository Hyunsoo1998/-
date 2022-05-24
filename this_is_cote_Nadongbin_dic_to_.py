#사전자료형
#사전자료형은 키(key)와 값(value)의 쌍을 데이터로 가지는 자료형
#키(key)값으로 값(value)에 접근 가능
#리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비된다.
#사전자료형은 키와값의 쌍을 데이터로 가지며, '변경불가능한 자료형'을 키(key)로 사용할수있다.

#파이썬의 사전자료형은 해시테이블을 이용하고, 데이터의 조회일 수정에 있어서 O(1)의 시간에 처리할수있다.

data=dict()
data['사과']='Apple'
data['바나나']='Banana'
data['코코넛']='Coconut'

if '사과' in data:
    print("'사과' 를 가지고 있는 데이터가 존재합니다.")

#사전자료형 관련 메서드
#사전자료형에서는 키(Key)와 값(value)을 별도로 뽑아내기 위한 메서드를 지웧난다.
#키 데이터만 뽑아서 리스트를 이용할때는 keys()함수를 이용한다.
#값 데이터만을 뽑아서 리스트로 이용할때는 values()함수를 이용한다

#키 데이터만 담은 리스트
key_list=data.keys()

#값 데이터만 담은 리스트
value_list=data.values()

print(key_list)
print(value_list)

#각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

a=dict()
a['홍길동']=97
a['이순신']=98

print(a)

#아래와 같은 방식으로도 사전자료형(key,value)으로 구성이 가능하다.
b={
    '홍길동':97,
    '이순신':98
}
print(b)
print(b['이순신'])

#특정 변수의 key 데이터만을 가져오고 싶을때
key_list= list(b.keys()) #key함수는 사전 key라는 하나의 객체로서
#반환 되기떄문에 list함수를 이용해서 list형 데이터로 형 변환을 수행한다.
print(key_list)

#집합 자료형
#-> 중복을 허용하지 않는다.  (중복된 원소를 제거해준다.)
#-> 순서가 없다.
#->집합은 리스트 혹은 문자열을 이용해서 초기화 할 수있다.


#집합 자료형 초기화 방법 1
data= set([1,1,2,3,4,4,5]) # list (혹은 문자열)를 set()함수를 이용해서
#초기화 할 수 있다. 이때 set()함수를 이용한다.

data={1,1,2,3,4,4,5}
print(data)

#집합 자료형의 연산
#기본적인 집합 연산으로 합집합,교집합 차집합 연산 등이 있다.

#1.합집합: 집합 A에 속하거나 B에 속하는 원소로 이루어진 집합
#2.교집합: 집합 A에 속하고 B에도 속하는 원소로 이루어진 집합
#3.차집합: 집합 A의 원소중에서 B에 속하지 않는 원소들로 이루어진 집합

a=set([1,2,3,4,5])
b=set([3,4,5,6,7])

#합집합
print(a|b)

#교집합
print(a&b)

#차집합
print(a-b)

#집합 자료형 관련 함수
data= set([1,2,3])

#새로운 원소 추가
data.add(4)
print(data)

#새로운 원소 여러 개 추가
data.update([5,6])
print(data)

#특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

#리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값에 접근 가능
#사전자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없고
#사전의 키(key)혹은 집합의 원소 element를 이용해 O(1)의 시간 복잡도로 조회한다

#기본 입출력

#모든 프로그램은 적절한 입출력 양식을 가지고 있다.
#프로그램 동작의 첫 번째 단계는 데이터를 입력받거나 생성하는 것이다.

#input()함수는 한줄의 문자열을 입력받는 함수
#map 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할때 사용한다.

#예시) 공백을 기준으로 구분된 데이터를 입력 받을때는 다음과 같이 사용한다.
#list(map(int,input().split()))
#예시) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면 다음과 같이 사용한다.
#a,b,c=map(int,input().split())

n=int(input())

#input()은 문자열로 입력을 받고, split()함수를 이용해 공백을 기준으로 데이터를 나눈다.

#각각의 데이터가 문자열로 들어있기 때문에 map함수를 이용해서 각각의 데이터를
#정수형으로 바꿔주고,
#list로 만들어 준다.
data=list(map(int,input().split()))

print(n)
print(data)

#데이터의 갯수가 정해져있다면 (예를들어 3개)
a,b,c=map(int,input().split())

print(a,b,c)

#사용자로부터 입력을 최대한 빠르게 받아야하는 경우

#파이썬의 경우 sys라이브러리에 정의되어있는 sys.stdin.readline()
#메서드를 이용한다.
#단 ,입력후 엔터(enter)가 줄 바꿈 기호로 입력되므로 rstrip()메서드를 함께 이용한다.

#빠르게 입력 받기
import sys

#문자열 입력 받기
data=sys.stdin.readline().rstrip()
print(data)

#자주 사용되는 표준 출력 방법

#출력할 변수들
a=1
b=2
print(a,b)
# 7,8을 출력할때 줄바꿈을 원치 않으므로 end=" " 을 이용해 줄바꿈을 하지 않고, 한칸띄워서 출력한다.

print(7, end=" ")
print(8, end=" ")


#출력할 변수
answer= 7
#정수형 데이터를 문자열 데이터로 바꾸고 출력한다.
print("정답은"+str(answer)+"입니다.")

#f-string 예제
#문자열 앞에 접두사 'f'를 붙여 사용한다.
#중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있다.
answer=7
print(f"정답은 {answer}입니다.")

