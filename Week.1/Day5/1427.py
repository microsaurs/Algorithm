# 문제 : 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
# 조건 : 첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다. 
#       첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

# 파이썬 sort 함수
# List.sort() -> list 객체 자체를 정렬해주는 함수
# list.sort()함수는 기본적으로 리스트를 오름차순으로 정렬해주는 기능
# 디폴트 값으로 list.sort(reverse=False)라서 이것이 오름차순인데 내림차순을 나타내고 싶으면 list.sort(reverse=True)를 이용하면 됨

N=int(input())

list = []
for i in str(N):
    list.append(int(i))

list.sort(reverse=True) #내림차순을 나타내는 sort 함수

for i in list:
    print(i,end="")