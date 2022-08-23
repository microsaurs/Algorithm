# 문제 : 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
#       등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
#       N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
# 조건 : 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
#       첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

X = int(input())
Y = 0

for i in range(1, X+1):
    if i <= 99: # 1-99까지는 전부 다 한수
        Y += 1
    else:
        Z = list(map(int, str(i))) #str(i) -> 숫자의 각 자릿수를 분리 / list에 들어가는 수의 각자리 수는 int로 배열에 들어감
        if Z[0] - Z[1] == Z[1] - Z[2]: #등차수열인지 확인하기
            Y += 1
print(Y)