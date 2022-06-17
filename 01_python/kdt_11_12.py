import os

T = int(input())
TT = int(input())
TTT = int(input())

for tc in range(1, T+1):
    answer = ''
    if answer == '':
        answer = True
    elif answer != '':
        answer = False
        
    print('#{} {}' .format(tc, answer))
    