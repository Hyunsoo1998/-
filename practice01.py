# # # # # a= 0.3 + 0.6

# # # # # print(round(a, 4))

# # # # # if(round(a,4)==0.9):
# # # # #     print(True)
# # # # # else:
# # # # #     print(False)
# # # # # c= 7
# # # # # b=3
# # # # # #나누기
# # # # # print(c/b) #파이썬에서 나누기연산자 (/)는 나눠진 결과를 기본적으로 실수형으로 처리한다.

# # # # # #나머지
# # # # # print(c%b)

# # # # # #몫
# # # # # print(c//b)

# # # # # #거듭제곱 연산자
# # # # # d=5
# # # # # e=3
# # # # # print(d**b) # d^e을 의미한다.

# # # # a=[1,2,3,4,5,6,7,8,9]
# # # # print(a)

# # # # # 인덱스 2  즉 3번째 원소에 접근
# # # # print(a[2])

# # # # #빈 리스트 선언 방법1
# # # # b=list()
# # # # print(b)
# # # # # 빈 리스트 선언 방법 2
# # # # c=[]
# # # # print(c)

# # # # #크기가 N이고 모든 값이 0인 1차원 리스트 초기화
# # # # n=10
# # # # a=[0]*n
# # # # print(a)

# # # a=[1,2,3,4,5,6,7,8,9]
# # # #두번째 원소부터 네번째 원소까지
# # # print(a[1:4])
# # # #0부터 19까지 홀수만 포함하는 리스트
# # # array=[i for i in range(20) if i%2==1]
# # # print(array)

# # # #1부터 9까지 수의 제곱값을 포함하는 리스트
# # # array=[i*i for i in range(1,10)]
# # # print(array)
# # # #리스트 컴프리헨션을 이용한 2차원 배열 초기화
# # # n= 3
# # # m=4
# # # array=[[0]*m for _ in range(n)]
# # # print(array)

# # a=[1,4,3]
# # print("기본 리스트: {}".format(a))

# # #리스트에 원소 삽입
# # a.append(2)
# # print("삽입 : ",a)

# # #오름차순 정렬
# # a.sort()
# # print("오름차순 정렬: ",a)
# # #내림차순 정렬
# # a.sort(reverse=True)
# # print("내림차순 정렬: ",a)
# # #리스트 원소 뒤집기
# # a.reverse()
# # print("원소뒤집기: ",a)

# # #특정 인덱스에 데이터 추가
# # a.insert(2,3)
# # print("인덱스 2에 3 추가: ",a)

# # #특정 값인 데이터 개수 새기
# # print("값이 3인 데이터 개수: ",a.count(3))

# # #특정 값 데이터 삭제
# # a.remove(1)
# # print("값이 1인 데이터 삭제: ",a)

# a=[1,2,3,4,5,5,5]
# remove_set = {3,5}

# #remove_set에 포함되지 않은 값만을 저장

# result= [i for i in a if i not in remove_set]
# print(result)

# data= "Hello World"
# print(data)

# data= "Don't you know \"PyThon\"?"
# print(data)

# a="Hello"
# b="World"
# print(a+""+b)
# a="String"
# print(a*3)

# a="ABCDEF"
# print(a[2:4])

# data= dict()
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'

# #키 데이터만 담은 리스트
# key_list = data.keys()
# #value (값)만 담은 리스트
# value_list = data.values()
# print(key_list)
# print(value_list)

# #각 키에 따른 값을 하나씩 출력
# for key in key_list:
#     print( data[key])

# if '사과' in data:
#     print("'사과'를 키로 가지는 데이터가 존재합니다.")


#집합 자료형 초기화 방법 1
# data= set([1,1,2,3,4,5])
# print(data)

# #집합 자료형 초기화 방법2
# data ={1,1,2,3,4,4,5}
# print(data)

# #집합 자료형의 연산
# a=set([1,2,3,4,5])
# b=set([3,4,5,6,7])
# print(a|b) # 합집합
# print(a&b) # 교집합
# print(a-b) # 차집합

data = set([1,2,3])
print(data)

#새로운 원소 추가
data.add(4)
print(data)

#새로운 원 소여러개 추가
data.update([5,6])
print(data)

#특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)