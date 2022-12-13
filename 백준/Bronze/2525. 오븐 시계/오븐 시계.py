A, B = map(int, input().split())
C = int(input())
D = (B+C)//60

if(B+C < 60):
    print(A, B+C)
elif(B+C >= 60 and A + D >= 24):
    print(A+D-24, (B+C)-60*D)
else:
    print(A+D, (B+C)-60*D)