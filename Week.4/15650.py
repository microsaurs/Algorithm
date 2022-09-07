# 문제 : 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#       1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 고른 수열은 오름차순이어야 한다.
# 조건 : 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
#       수열은 사전 순으로 증가하는 순서로 출력해야 한다.

N,M = list(map(int,input().split()))
s = []
def sequence(start): # start 변수 추가 / 전에 방문한 노드보다 큰 노드만 방문하기 위해 파라미터로 전달(변수 추가 이유)
    if len(s)==M: # 함수 탈출 조건
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,N+1): # 앞의 숫자가 뒤의 숫자보다 작은 경우를 제외하기 위해 start부터 N까지 숫자 사용
        if i not in s:
            s.append(i)
            sequence(i+1) # 오름차순으로 리스트에 들어가게 됨
            s.pop()

sequence(1)