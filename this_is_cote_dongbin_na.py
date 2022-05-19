#리스트 컴프리 헨션

array=[i for i in range(10) if i%2==0]
print(array)

# NXM크기의 2차원 리스트 초기화
n=4
m=3
array=[[0]*m for _ in range(n)]
print(array)

#리스트 관련 기타 메서드
a=[1,4,3]
print("기본 리스트 :",a)

#리스트에 원소 삽입
a.append(2)
print("삽입: ",a)

#오름차순 정렬
a.sort()
print("오름차순 정렬: ",a)

#내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬:",a)

#리스트 원소 뒤집기

a=[4,3,2,1]
a.reverse()
print("원소 뒤집기: ",a)

#특정 인덱스에 데이터 추가
a.insert(2,3)
print("인덱스 2에 3추가: ",a)

#특정값인 데이터 개수 세기( 변수명.count())
print("값이 3인 데이터 개수: ",a.count(3))

#특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ",a)

#문자열 자료형
data="Hello World"
print(data)

data = "Don't you know \"Python\"?"
print(data)

a="Hello"
b="World"
print(a+ " "+ b)

a="String"
print(a*3)

a="ABCDEF"
print(a[2:4])
#문자열은 특정한 인덱스 값을 변경 할 수없다.

#튜플 사용 예제
a=(1,2,3,4,5,6,7,8,9)

#네 번째 원소만 출력
print(a[3])

#두 번째 원소부터 네 번째 원소까지
print(a[1:4])

#튜플 사용 예제(오류가 발생하는예제)
#튜플은 한번 지정된 값을 변경 할 수없다
# a=(1,2,3,4)
# print(a)
# a[2]=7 >> 오류 발생: 튜플은 한번 지정된 값 변경 불가 immutable