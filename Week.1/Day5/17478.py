# 문제 : 평소에 질문을 잘 받아주기로 유명한 중앙대학교의 JH 교수님은 학생들로부터 재귀함수가 무엇인지에 대하여 많은 질문을 받아왔다.
#       매번 질문을 잘 받아주셨던 JH 교수님이지만 그는 중앙대학교가 자신과 맞는가에 대한 고민을 항상 해왔다.
#       중앙대학교와 자신의 길이 맞지 않다고 생각한 JH 교수님은 결국 중앙대학교를 떠나기로 결정하였다.
#       떠나기 전까지도 제자들을 생각하셨던 JH 교수님은 재귀함수가 무엇인지 물어보는 학생들을 위한 작은 선물로 자동 응답 챗봇을 준비하기로 했다.
#       JH 교수님이 만들 챗봇의 응답을 출력하는 프로그램을 만들어보자.
# 조건 : 교수님이 출력을 원하는 재귀 횟수 N(1 ≤ N ≤ 50)이 주어진다.


# 가장 먼저 대답을 출력하는 함수를 선언해준다.
def chatbot(i,n):
    print("____"*i + '"재귀함수가 뭔가요?"')
    if i == n: # 재귀함수 ~ 함수라네 라는 대답은 마지막에 하는 대답이기 때문에 i==n이 될 때 출력
        print("____"*i + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else: # i != n 일 때에는 ____에 i를 곱한만큼 먼저 출력해주고 그 뒤에 문장을 출력
        print("____"*i + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print("____"*i + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print("____"*i + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        chatbot(i+1,n) # i == n이 될 때까지 반복해주는 용도로 chatbot함수를 한 번 더 호출
    print("____"*i +"라고 답변하였지.")

#n을 입력받고 질문을 출력한 뒤 자동 답변이 나오는 함수를 호출
n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
chatbot(0,n)