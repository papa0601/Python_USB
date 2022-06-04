from random import randint
from time import sleep

def cls():
    from os import system
    system('cls')

listerr = ['이미 사용된 위치입니다.', '입력이 올바르지 않습니다.']

while True:
    listnum = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    liststr = ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)']

    num = randint(0, 1)
    if num == 0:
        order = 0
        plr = 1
        opp = -1
        plricon = 'O'
        oppicon = 'X'


    else:
        order = 1
        plr = -1
        opp = 1
        plricon = 'X'
        oppicon = 'O'

     #  게임의 메인 코드입니다.

    while True:  #  수로 이로어진 위치데이터를 글자로 변환합니다.
        for i in range(9):
            if listnum[i] == 0:
                liststr[i] = i + 1

            elif listnum[i] == 1:
                liststr[i] = 'O'

            elif listnum[i] == -1:
                liststr[i] = 'X'

        if order == 0:
            orderstr = '당신'
            iconstr = plricon
        elif order == 1:
            orderstr = '상대방'
            iconstr = oppicon

        print(orderstr + '(' + iconstr + ')' + '의 차례입니다.') #  현재 배치 상태를 표시합니다.
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
                    decision = int(input('어느 곳에 둘까요?(1~9)>>>').replace('.0', '')) -1

                    if listnum[decision] == 0:
                        if decision < 0 or decision > 10:
                            raise(ZeroDivisionError)
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
                placeimportance = [1, 1, 1, 1, 1, 1, 1, 1, 1] #  중요도 리스트

                if horizontal1 == plr*2 or horizontal1 == opp*2: #  상대의 우승 방해 또는 자신의 우승 확정
                    for x in range(0, 3):
                        if listnum[x] == 0 and horizontal1 == plr*2:
                            placeimportance[x] = 3

                        else:
                            placeimportance[x] = 4

                elif horizontal2 == plr*2 or horizontal2 == opp*2:
                    for x in range(3, 6):
                        if listnum[x] == 0 and horizontal2 == plr * 2:
                            placeimportance[x] = 3

                        else:
                            placeimportance[x] = 4

                elif horizontal3 == plr*2 or horizontal3 == opp*2:
                    for x in range(6, 9):
                        if listnum[x] == 0 and horizontal3 == plr * 2:
                            placeimportance[x] = 3

                        else:
                            placeimportance[x] = 4

                elif longitude1 == plr * 2 or longitude1 == opp * 2:
                    for x in range(0, 7, 3):
                        if listnum[x] == 0 and longitude1 == plr * 2:
                            placeimportance[x] = 3

                        else:
                            placeimportance[x] = 4

                elif longitude2 == plr * 2 or longitude2 == opp * 2:
                    for x in range(1, 8, 3):
                        if listnum[x] == 0 and longitude2 == plr * 2:
                            placeimportance[x] = 3

                        else:
                            placeimportance[x] = 4

                elif longitude3 == plr * 2 or longitude3 == opp * 2:
                    for x in range(2, 9, 3):
                        if listnum[x] == 0 and longitude3 == plr * 2:
                            placeimportance[x] = 3

                        else:
                            placeimportance[x] = 4

                elif diagonal1 == plr * 2 or diagonal1 == opp * 2:
                    for x in range(0, 9, 4):
                        if listnum[x] == 0 and diagonal1 == plr * 2:
                            placeimportance[x] = 3

                        else:
                            placeimportance[x] = 4

                elif diagonal2 == plr * 2 or diagonal2 == opp * 2:
                    for x in range(2, 7, 2):
                        if listnum[x] == 0 and diagonal2 == plr * 2:
                            placeimportance[x] = 3

                        else:
                            placeimportance[x] = 4

                for i in range(9): #  이미 설치된 자리의 중요도 제거
                    if listnum[i] == 1 or listnum[i] == -1:
                        placeimportance[i] = 0

                print(placeimportance)

                highimportance = 0  #  가장 높은 정확도를 산출
                for i in range(9):
                    if placeimportance[i] > highimportance:
                        highimportance = placeimportance[i]
                print('최고 중요도' + str(highimportance))


                decisionlist = [] #  가능하면서 가장 중요한 동작을 산출
                for i in range(9):
                    if placeimportance[i] == highimportance:
                        decisionlist.append(i)

                print(decisionlist)

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

        elif listnum[0] != 0 and listnum[1] != 0 and listnum[2] != 0 and listnum[3] != 0 and listnum[4] != 0 and listnum[5] != 0 and listnum[6] != 0 and listnum[7] != 0 and listnum[8] != 0:
            winner = 'draw'

    cls()
    for i in range(9):
        if listnum[i] == 0:
            liststr[i] = '-'

        elif listnum[i] == 1:
            liststr[i] = 'O'

        elif listnum[i] == -1:
            liststr[i] = 'X'

    if winner == 'draw':
        print('무승부 입니다')
    else:
        print(winner + '의 승리입니다!')
    print('')
    print(' ' + str(liststr[0]) + ' | ' + str(liststr[1]) + ' | ' + str(liststr[2]))
    print('——— ——— ———')
    print(' ' + str(liststr[3]) + ' | ' + str(liststr[4]) + ' | ' + str(liststr[5]))
    print('——— ——— ———')
    print(' ' + str(liststr[6]) + ' | ' + str(liststr[7]) + ' | ' + str(liststr[8]))
    print('')
    re = input('다시 하시겠습니까?(y/n)>>>')
    if re == 'y':
        cls()
    else:
        break