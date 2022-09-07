# 문제 : 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 조건 : 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.
#       첫째 줄에 N!을 출력한다.

# 함수선언
# def function_name ( parameter ):
    # code
# 재귀함수
# 정의 단계에서 자신을 재참조하는 함수를 뜻한다.

def factorial(n):
    fac = 1
    if n>0:
        fac = n * factorial(n-1)
    return fac

N = int(input())
print(factorial(N))