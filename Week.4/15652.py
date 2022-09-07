# 문제 : 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#       1부터 N까지 자연수 중에서 M개를 고른 수열
#       같은 수를 여러 번 골라도 된다.
#       고른 수열은 비내림차순이어야 한다.
#       길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
# 조건 : 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
#       수열은 사전 순으로 증가하는 순서로 출력해야 한다.

N,M = map(int,input().split())
s = []

def sequence():

    #s의 길이가 M이 되면 print
    if len(s) == M:
        print(' '.join(list(map(str,s))))
    else:
        for i in range(1, N+1):
            #s가 비어있으면 그냥 추가
            if not s:
                s.append(i)
                sequence()
                s.pop()
            elif s[-1] <= i: #그렇지 않으면 s의 마지막 원소보다 크거나 같을 때만 추가 / s[-1]은 s리스트의 마지막 요솟값을 말함
                s.append(i)
                sequence()
                s.pop()

sequence()