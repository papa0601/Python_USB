from random import randint
from time import sleep

def cls():
    from os import system

    system('cls')

time = 1

errcode = ''
while True:
    print('=' * 15)
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
            print('=' * 15)
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
        break

    elif answer == 'NyanCat' or answer == 'nyancat' or answer == 'Nyancat':
        task = 'cat'
        cls()

    else:
        errcode = ' - [선택지가 잘못되었습니다]'
        cls()

    break

errcode = ''
while True:
    if task == 1 or task == 2:
        print('=' * 15)
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
            for i in range(7):
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

if task == 1:
    while True:
        refresh = 0
        for i in range(repeat):
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
                    refresh += 1


            else:
                if way == 1:
                    small = list[i + 1]
                    big = list[i]
                    print('앞[' + str(list[i]) + '] > 뒤[' + str(list[i + 1]) + '] >>> 순서 바꾸기!')
                    list[i] = small
                    list[i + 1] = big
                    comparetime += 1
                    exchangetime += 1
                    refresh += 1

                else:
                    comparetime += 1
                    print('앞[' + str(list[i]) + '] ≥ 뒤[' + str(list[i + 1]) + '] >>> 넘어감')
            print('')
            sleep(time)
            cls()
        if refresh == 0:
            comparetime -= (len(list) - 1)
            break

elif task == 2:
    pass

elif task == 3:
    pass

elif task == 'cat':
    pass

cls()

if task == 1 or task == 2:
    print('정렬 방법: ' + displaymode + ' / 정렬 순서: ' + displayway)
    print('')
    print('원본 :', original,end = ' -> ')
    print('정렬 결과 :', list)
    print('')
    print('비교 횟수: ', comparetime,end = ' / ')
    print('교환 횟수: ', exchangetime)
    input()