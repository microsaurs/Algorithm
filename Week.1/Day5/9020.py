# 문제 : 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 
#       예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.
#       골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 
#       이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 
#       예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.      #       10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
#       2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 
#       만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
# 조건 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.
#       각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

# 파이썬 sqrt() 제곱근 함수
# math.sqrt(n) -> n의 제곱근을 반환 (float형태로 출력)

# 1. n이하의 숫자들 중 소수 찾기 (에라토스테네스의 체)
def prime_list(n):
    # 에라토스테네스의 체 초기화 : n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:    # i가 소수인 경우
            for j in range(i+i, n, i):  #i이후 i의 배수들을 False 판정
                sieve[j] = False
    
    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

# 2. n이하의 소수들 중 합이 n
def sosu(n):
    li=prime_list(n)
    idx = max([i for i in range(len(li)) if li[i]<=n/2])
    for i in range(idx,-1,-1):
        for j in range(i,len(li)):
            if li[i]+li[j]==n:
                return [li[i],li[j]]

for _ in range(int(input())):
    n=int(input())
    print(" ".join(map(str,sosu(n))))