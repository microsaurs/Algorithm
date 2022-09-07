# 문제 : N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
#       N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
# 조건 : 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

# 파이썬 abs : 절대 값 함수 

import sys

count = 0

# 퀸을 놓으려면 놓으려는 자리에 가로,세로,대각선에 다른 퀸이 없는지 확인
def check(x):
    for i in range(x):
        if visited[x] == visited[i] or abs(visited[x] - visited[i]) == x - i:
            return False

def queen(x,n):
    global count #전역변수 설정
    if x == n: #마지막까지 탐색
        count += 1 # 값 증가
    else:
        for i in range(n):
            visited[x] = i
            if check(x):
                queen(x + 1, n)

n = int(sys.stdin.readline())
visited = [0] * n # 크기가 n인 1차원 리스트 초기화
queen(0,n)
print(count)
