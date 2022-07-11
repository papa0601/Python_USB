from random import randint
from time import sleep

def cls():
    from os import system

    system('cls')

lcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']
ucase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
schr = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '|', ';', '-', '_', '+', '=', '?', ':']
time = 0.2

errcode = ''
while True:
    print('=' * 25)
    print('[수행할 작업을 선택해주세요]' + errcode)
    print('1. 버블 정렬 (Bubble Shuffle)')
    print('2. 선택 정렬 (Selection Shuffle)')
    print('3. 비밀번호 유효성 검사 (Password Validation)')
    print('')
    answer = input('>>>')

    if answer == '1' or answer == '2':
        if answer == '1':
            displaymode = '버블 정렬'
            task = 1

        else:
            displaymode = '선택 정렬'
            task = 2

        cls()
        errcode = ''
        while True:
            print('=' * 25)
            print('-(' + displaymode + ')')
            print('')
            print('[정렬 순서를 선택해주세요]' + errcode)
            print('1. 오름차순 (Ascending)')
            print('2. 내림차순 (Descending)')
            print('')
            answer = input('>>>')

            if answer == '1':
                displayway = '오름차순'
                way = 1
                cls()
                break

            elif answer == '2':
                displayway = '내림차순'
                way = 2
                cls()
                break

            else:
                errcode = ' - [선택지가 잘못되었습니다]'
                cls()

    elif answer == '3':
        task = 3
        cls()
        

    elif answer == 'NyanCat':
        task = 'cat'
        cls()
        

    else:
        errcode = ' - [선택지가 잘못되었습니다]'
        cls()

    break
cls()
pmode = 0
listlength = 30
print('발표모드를 켜시겠습니까?')
print('발표모드 활성화 시..')
print('▶랜덤 리스트의 길이가 7칸이 됩니다(기본 30칸)')
print('▶자동 넘어가기가 비활성화 됩니다.')
print('')
answer = input('(y/n)>>>')
if answer == 'y':
    listlength = 7
    pmode = 1
cls()

if pmode == 0:
    while True:
        print('sleep시간을 설정해주세요.', errcode)
        print('숫자로 입력하세요')
        print('공백으로 0초로 설정합니다.')
        print('')
        answer = input('>>>')

        if answer == '':
            time = 0
            break
        else:
            try:
                time = float(answer)
                break
            except:
                errcode = ' - [입력이 올바르지 않습니다]'
                cls()


errcode = ''
cls()
if task == 1 or task == 2:
    while True:
        print('=' * 25)
        print('-(' + displaymode + ') -(' + displayway + ')')
        print('')
        print('[정렬할 리스트를 입력해주세요]' + errcode)
        print('▶정렬할 리스트는 정수로 구성되어야합니다.')
        print('▶정렬할 리스트의 요소는 공백(띄어쓰기)으로 구분합니다.')
        print('')
        print('또는, 리스트를 자동으로 생성할 수 있습니다. 이 경우 -100 ~ 100사이의 임의의 수로 구성된 7칸의 리스트가 생성됩니다.')
        print('▶리스트를 자동으로 생성하려면 r을 입력하세요.')
        answer = input('>>>').replace(',', '')

        list = []
        original = []
        if answer == 'r':
            for i in range(listlength):
                rannum = (randint(-100, 100))
                list.append(rannum)
                original.append(rannum)
            cls()
            break

        else:
            templist = answer.split()
            if len(templist) < 4:
                errcode = ' - [리스트가 너무 짧습니다. 최소 4개 이상의 요소로 구성된 리스트를 입력해주세요.]'
                lengthtest = 0
                cls()

            elif len(templist) > 20:
                errcode = ' - [리스트가 너무 깁니다. 리스트의 요소가 20개 이하가 되도록 다시 입력해주세요.]'
                lengthtest = 0
                cls()

            else:
                lengthtest = 1


            try:
                int(answer.replace(' ', ''))
                indextest = 1
            except:
                errcode = ' - [리스트가 정수로 이루어지지 않았습니다]'
                indextest = 0
                cls()

            if lengthtest * indextest == 1:
                list = answer.split()
                original = answer.split()
                cls()
                break


    comparetime = 0
    exchangetime = 0
    repeat = len(list) - 1
    attempt = 0

    if task == 1:
        while True:
            for i in range(repeat - attempt):

                for x in range(len(list)):
                    if x == i:
                        print( '    >[' + str(list[x]) + ']', end='')

                    elif x == i + 1:
                        print( '[' + str(list[x]) + ']<    ', end='')

                    else:
                        print('[' + str(list[x]) + ']', end=' ')

                print('\n')
                print('비교 횟수: ' + str(comparetime) + ' / 교환 횟수: '+ str(exchangetime))
                print('\n')
                print(str(i + 1) + '.',end ='')


                if list[i] <= list[i + 1]:
                    if way == 1:
                        comparetime += 1
                        print('앞[' + str(list[i]) + '] ≤ 뒤[' + str(list[i + 1]) + '] >>> 넘어감')

                    else:
                        small = list[i]
                        big = list[i + 1]
                        print('앞[' + str(list[i]) + '] < 뒤[' + str(list[i + 1]) + '] >>> 순서 바꾸기!')
                        list[i] = big
                        list[i + 1] = small
                        comparetime += 1
                        exchangetime += 1


                else:
                    if way == 1:
                        small = list[i + 1]
                        big = list[i]
                        print('앞[' + str(list[i]) + '] > 뒤[' + str(list[i + 1]) + '] >>> 순서 바꾸기!')
                        list[i] = small
                        list[i + 1] = big
                        comparetime += 1
                        exchangetime += 1

                    else:
                        comparetime += 1
                        print('앞[' + str(list[i]) + '] ≥ 뒤[' + str(list[i + 1]) + '] >>> 넘어감')
                print('')
                if pmode == 1:
                    input('>')
                else:
                    sleep(time)
                cls()

            if repeat - attempt == 0:
                break


            attempt += 1


    elif task == 2:
        for i in range(len(list) - 1): #박스를 설정하는 거라고 보셈 한마디로 처음에 최솟값을 제공하는 칸이다 이말이야 /  이녀석은 리스트의 길이 - 1만큼 반복해야지 왜냐하면 마지막 칸은 선택할 필요가 없으니까
            min = list[i] #일단 비교대상 1순위 (첫번째 칸)에 있는 녀석을 최솟값으로 둬야지
            minloca = i

            for k in range(len(list) - i - 1): #이 친구는 최솟값과 다른 값들을 비교를 하겠지? 그 때 몇 번째 칸과 비교를 할지 정해주는 녀석이야 / 이녀석은 리스트의 길이 - i를 해야해 i가 밀리면 얘도 밀리니까
                for x in range(len(list)):
                    if way == 1:
                        check = k + i + 1
                    else:
                        check = len(list) - k - 1

                    if x == i:
                        print('/[', list[x], ']/', end=' ')

                    elif x == check or x == minloca:
                        print('>[', list[x], ']<', end=' ')

                    else:
                        print('[', list[x], ']', end=' ')
                print('')
                print('\n')
                print('비교 횟수: ' + str(comparetime) + ' / 교환 횟수: ' + str(exchangetime))
                print('\n')
                if way == 1:
                    if list[check] < min:
                        print('최솟값: ', min, ' > 비굣값', list[check], ' >>> 최솟값을 변경!')
                        min = list[check]
                        minloca = check
                        comparetime += 1

                    elif list[check] >= min:
                        print('최솟값: ', min, ' ≤ 비굣값', list[check], ' >>> 최솟값을 유지')
                        comparetime += 1

                else:
                    if list[check] >= min:
                        print('최댓값: ', min, ' < 비굣값', list[check], ' >>> 최댓값을 변경!')
                        min = list[check]
                        minloca = check
                        comparetime += 1

                    elif list[check] < min:
                        print('최댓값: ', min, ' ≥ 비굣값', list[check], ' >>> 최댓값을 유지')
                        comparetime += 1

                if pmode == 1:
                    input('>')
                else:
                    sleep(time)
                cls()

            for x in range(len(list)):
                if x == i:
                    print('/[', list[x], ']/', end=' ')

                elif x == minloca:
                    print('>[', list[x], ']<', end=' ')

                else:
                    print('[', list[x], ']', end=' ')

            print('')
            print('\n')
            print('비교 횟수: ' + str(comparetime) + ' / 교환 횟수: ' + str(exchangetime))
            print('\n')
            if min != list[i]: # 이 알고리즘으로 가장 작은 놈이랑 가장 큰 놈을 바꾸는 거야
                big = list[i]
                small = list[minloca]
                print(list[i], '(와)과 ', min, '의 위치를 바꾼다!')
                list[i] = small
                list[minloca] = big
                exchangetime += 1

            else:
                print('바꿀 필요가 없다')

            if pmode == 1:
                input('>')
            else:
                sleep(time)
            cls()



if task == 3:
    errcode = ''
    while True:
        print('[사용하실 비밀번호를 입력해주세요]', errcode)
        print('비밀번호는...')
        print('▶8자리에서 16자리 사이여야 합니다.')
        print('▶영어 대/소문자와 특수문자 그리고 숫자로만 구성되어야 합니다.')
        print('▶특수문자와 대문자 숫자 중 최소 2개를 포함해야 합니다.')
        print('')
        password = input('>>>')
        copypassword = password

        if 8 <= len(str(password)) <= 16:
            checklength = 1
            checklengthp = 'O'
        else:
            checklength = 0
            checklengthp = 'X'

        for i in range(len(lcase)):
            copypassword = copypassword.replace(lcase[i], '')
            copypassword = copypassword.replace(ucase[i], '')
        for i in range(len(num)):
            copypassword = copypassword.replace(num[i], '')
        for i in range(len(schr)):
            copypassword = copypassword.replace(schr[i], '')

        if len(copypassword) == 0:
            contents = 1
            contentsp = 'O'
        else:
            contents = 0
            contentsp = 'X'

        ucasein = 0
        numin = 0
        schrin = 0
        for i in range(len(ucase)):
            if password.find(ucase[i]) != -1:
                ucasein = 1
                break
        for i in range(len(num)):
            if password.find(num[i]) != -1:
                numin = 1
                break
        for i in range(len(schr)):
            if password.find(schr[i]) != -1:
                schrin = 1
                break
        if ucasein + numin + schrin >= 2:
            concheckp = 'O'
        else:
            concheckp = 'X'

        if checklength == 1 and contents == 1 and ucasein + numin + schrin >= 2:
            cls()
            input('✔사용 가능한 비밀번호입니다.')
            break

        else:
            cls()
            print('❌사용할 수 없는 비밀번호입니다.')
            print('길이가 6~12인가? : ', checklengthp)
            print('사용할 수 있는 문자만 포함하는가? : ', contentsp)
            print('숫자, 대문자, 특수문자 중 두개 이상 포함하는가? : ',concheckp )
            input()
            cls()

elif task == 'cat':
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
    sleep(0.05)
    print('░░░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░░')
    sleep(0.05)
    print('░░░░░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░░░░░')
    sleep(0.05)
    print('░░░░░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░░░░░')
    sleep(0.05)
    print('░░░░░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░░░░░')
    sleep(0.05)
    print('░░░░░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░░░░░')
    sleep(0.05)
    print('░░░░░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░░░░░')
    sleep(0.05)
    print('░░░░░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░░░░░')
    sleep(0.05)
    print('░░░░░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░░░░░')
    sleep(0.05)
    print('░░░░░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░░░░░')
    sleep(0.05)
    print('░░░░░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░░░░░')
    sleep(0.05)
    print('░░░░░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░░░░░')
    sleep(0.05)
    print('░░░░░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░░░░░')
    sleep(0.05)
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
    print('')
    sleep(0.05)
    print(' ______                                     ______           ______                  ')
    sleep(0.05)
    print('(_____ \                                   (____  \         (_____ \                 ')
    sleep(0.05)
    print(' _____) )___ ___   ____  ____ ____ ____     ____)  )_   _    _____) )___ ____   ____ ')
    sleep(0.05)
    print('|  ____/ ___) _ \ / _  |/ ___) _  |    \   |  __  (| | | |  |  ____/ _  |  _ \ / _  |')
    sleep(0.05)
    print('| |   | |  | |_| ( ( | | |  ( ( | | | | |  | |__)  ) |_| |  | |   ( ( | | | | ( ( | |')
    sleep(0.05)
    print('|_|   |_|   \___/ \_|| |_|   \_||_|_|_|_|  |______/ \__  |  |_|    \_||_| ||_/ \_||_|')
    sleep(0.05)
    print('                 (_____|                           (____/               |_|          ')
    input()

cls()
if task == 1 or task == 2:
    print('정렬 방법: ' + displaymode + ' / 정렬 순서: ' + displayway)
    print('')
    print('원본 :', original,end = ' -> ')
    print('정렬 결과 :', list)
    print('')
    print('비교 횟수: ', comparetime,end = ' / ')
    print('교환 횟수: ', exchangetime)

input('\n\n\n~Program Finished')