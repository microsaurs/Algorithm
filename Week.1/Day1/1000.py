# 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 조건 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
#       첫째 줄에 A+B를 출력한다.

#map()함수 = 여러 변수 값들에 함수를 동시에 적용시켜 값을 반환할 때 사용
#           이 문제에서는 값들을 정수형으로 형변환하는데 사용됨
#input()함수 = 문자열을 입력 받는 함수 (숫자를 입력해도 문자열로 인식)
#split()함수 = ()안에 있는 문자를 기준으로 문자열 분할 (()안에 아무것도 없으면 공백을 기준으로 함)

A,B = map(int,input().split())
print(A+B)


