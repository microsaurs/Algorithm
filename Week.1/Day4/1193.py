# 문제 : 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.(표 생략)
#       이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 
#       차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
#       X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 문제 이해
# 각 라인을 나눠서 보면 (1/1) (1/2, 2/1) (3/1, 2/2, 1/3) (1/4, 2/3, 3/2, 4/1) ... 이렇게 진행된다.
# 각 분수의 분자,분모는 각 라인 번호가 가장 큰 수임
# 입력받은 수에서 라인의 수를 1씩 증가시키면서 뺄셈을 해서 입력받은 수가 몇 라인의 몇 번째 숫자인지 구하기
# 홀수 라인은 분자가 내림차순, 분모가 오름차순 / 짝수 라인은 분자가 오름차순, 분모가 내림차순이므로 조건을 나눠서 출력

X = int(input()) # 숫자 입력 받음
line = 1 # 라인을 1로 초기화 시킴

while X>line:   # X번 째의 분수의 분모와 분자 중 가장 큰 수는 라인의 수
    X-=line     # X가 라인의 수보다 클 수 없기 때문에 X에서 라인 수를 빼주면서 X를 라인보다 작게 만들어준다.
                # (각 라인에 있는 분수의 갯수가 라인의 수이기 때문에 X에서 line을 빼주는 것, 그러면 X가 몇번째 숫자인지 알 수 있다.)
    line+=1     # X-line을 실행하고도 line의 수가 더 크면 line을 하나씩 증가시키면서 다음 라인으로 넘어간다.
if line%2==0:   # 라인이 분모분자의 최댓값이 되면 홀수라인인지 짝수라인인지에 따라 분수를 표현해줌
    a=X         # 짝수 라인은 분모가 오름차순, 분자가 내림차순이기 때문에 a=X
    b=line-X+1 
else:
    a=line-X+1
    b=X

print(a, '/',b,sep='')