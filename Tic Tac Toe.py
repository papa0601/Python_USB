from random import randint
from time import sleep

def cls():
    from os import system
    system('cls')

listnum = [0, 0, 0, 0, 0, 0, 0, 0, 0]
liststr = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
listerr = ['이미 사용된 위치입니다.', '입력이 올바르지 않습니다.']

AI = 0

 #  플레이어의 기호를 지정합니다.
num = randint(0, 1)
if num == 0:
    order = 0
    plr = 1
    opp = -1

else:
    order = 1
    plr = -1
    opp = 1

 #  게임의 메인 코드입니다.

while True:  #  수로 이로어진 위치데이터를 글자로 변환합니다.
    for i in range(9):
        if listnum[i] == 0:
            liststr[i] = '-'

        elif listnum[i] == 1:
            liststr[i] = 'O'
        
        elif listnum[i] == -1:
            liststr[i] = 'X'
        
    if order == 0:
        orderstr = '당신'
    elif order == 1:
        orderstr = '상대방'

    print(orderstr + '의 차례입니다.') #  현재 배치 상태를 표시합니다.
    print('')
    print(' ' + str(liststr[0]) + ' | ' + str(liststr[1]) + ' | ' + str(liststr[2]))
    print('——— ——— ———')
    print(' ' + str(liststr[3]) + ' | ' + str(liststr[4]) + ' | ' + str(liststr[5]))
    print('——— ——— ———')
    print(' ' + str(liststr[6]) + ' | ' + str(liststr[7]) + ' | ' + str(liststr[8]))

    horizontal1 = listnum[0] + listnum[1] + listnum[2]
    horizontal2 = listnum[3] + listnum[4] + listnum[5]
    horizontal3 = listnum[6] + listnum[7] + listnum[8]
    longitude1 = listnum[0] + listnum[3] + listnum[6]
    longitude2 = listnum[1] + listnum[4] + listnum[7]
    longitude3 = listnum[2] + listnum[5] + listnum[8]
    diagonal1 = listnum[0] + listnum[4] + listnum[8]
    diagonal2 = listnum[2] + listnum[4] + listnum[6]
    
    if order == 0: #  플레이어가 둘 곳을 입력합니다.
        while True:
            try:
                decision = int(input('어느 곳에 둘까요?(1~9)>>>')) -1

                if listnum[decision] == 0:
                    listnum[decision] = plr
                    cls()
                    order = 1
                    break

                else:
                    cls()
                    print(listerr[0])

            except:
                cls()
                print(listerr[1])

    else: #  컴퓨터가 둘 곳을 선택합니다. #TODO 추후 AI를 넣을 예정입니다.
        while True:
            decision = randint(1, 9) -1

            if AI == 1:
                placeimportance = [1, 1, 1, 1, 2, 1, 1, 1, 1] #  중요도 리스트

                for i in range(9): #  이미 설치된 자리의 중요도 제거
                    if listnum[i] == 0 or listnum[i] == -1:
                        placeimportance[i] = 0

                if horizontal1 == plr*2 or horizontal1 == opp*2: #  상대의 우승 방해 또는 자신의 우승 확정
                    for x in range(0, 2):
                        if listnum[x] == 0:
                            placeimportance[x] = 3

                elif horizontal2 == plr*2 or horizontal2 == opp*2:
                    for x in range(3, 5):
                        if listnum[x] == 0:
                            placeimportance[x] = 3

                elif horizontal3 == plr*2 or horizontal3 == opp*2:
                    for x in range(6, 8):
                        if listnum[x] == 0:
                            placeimportance[x] = 3

                elif longitude1 == plr * 2 or longitude1 == opp * 2:
                    for x in range(0, 6, 3):
                        if listnum[x] == 0:
                            placeimportance[x] = 3

                elif longitude2 == plr * 2 or longitude2 == opp * 2:
                    for x in range(1, 7, 3):
                        if listnum[x] == 0:
                            placeimportance[x] = 3

                elif longitude3 == plr * 2 or longitude3 == opp * 2:
                    for x in range(2, 8, 3):
                        if listnum[x] == 0:
                            placeimportance[x] = 3

                elif diagonal1 == plr * 2 or diagonal1 == opp * 2:
                    for x in range(1, 8, 4):
                        if listnum[x] == 0:
                            placeimportance[x] = 3

                elif diagonal1 == plr * 2 or diagonal1 == opp * 2:
                    for x in range(2, 6, 2):
                        if listnum[x] == 0:
                            placeimportance[x] = 3

                highimportance = 0  #  가장 높은 정확도를 산출
                for i in range(8):
                    if placeimportance[i] > highimportance:
                        highimportance = placeimportance[i]
                print('최고 중요도' + str(highimportance))

                decisionlist = [] #  가능하면서 가장 중요한 동작을 산출
                for i in range(8):
                    if placeimportance[i] == highimportance:
                        decisionlist.append(i)


                decisionlistlenght = len(decisionlist) #  동작 중 하나를 선택
                chooser = randint(1, decisionlistlenght) -1
                decision = decisionlist[chooser]
            print('결론' + str(decision))

            if listnum[decision] == 0:
                listnum[decision] = opp
                order = 0
                sleep(0.5)
                cls()
                break
            sleep(100)

    horizontal1 = listnum[0] + listnum[1] + listnum[2]
    horizontal2 = listnum[3] + listnum[4] + listnum[5]
    horizontal3 = listnum[6] + listnum[7] + listnum[8]
    longitude1 = listnum[0] + listnum[3] + listnum[6]
    longitude2 = listnum[1] + listnum[4] + listnum[7]
    longitude3 = listnum[2] + listnum[5] + listnum[8]
    diagonal1 = listnum[0] + listnum[4] + listnum[8]
    diagonal2 = listnum[2] + listnum[4] + listnum[6]

    if horizontal1 == plr*3 or horizontal2 == plr*3 or horizontal3 == plr*3 or longitude1 == plr*3 or longitude2 == plr*3 or longitude3 == plr*3 or diagonal1 == plr*3 or diagonal2 == plr*3:
        winner = orderstr
        break

    elif horizontal1 == opp*3 or horizontal2 == opp*3 or horizontal3 == opp*3 or longitude1 == opp*3 or longitude2 == opp*3 or longitude3 == opp*3 or diagonal1 == opp*3 or diagonal2 == opp*3:
        winner = orderstr
        break

cls()
for i in range(9):
    if listnum[i] == 0:
        liststr[i] = '-'

    elif listnum[i] == 1:
        liststr[i] = 'O'

    elif listnum[i] == -1:
        liststr[i] = 'X'

print(winner + '의 승리입니다!')
print('')
print(' ' + str(liststr[0]) + ' | ' + str(liststr[1]) + ' | ' + str(liststr[2]))
print('——— ——— ———')
print(' ' + str(liststr[3]) + ' | ' + str(liststr[4]) + ' | ' + str(liststr[5]))
print('——— ——— ———')
print(' ' + str(liststr[6]) + ' | ' + str(liststr[7]) + ' | ' + str(liststr[8]))