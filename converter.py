
def cls():
    from os import system
    system('cls')

while True:
    mode = input('[작업을 선택해주세요]\n'
                '1. 10진수 -> n진수 변환\n'
                '2. n진수 -> 10진수 변환\n'
                '>>>')
    if mode == '1':
        while True:
            try:
                number = int(input('변환할 숫자를 입력해주세요>>>'))
                while True:
                    numtype = int(input('변환할 진법을 입력해주세요(2~16)>>>'))
                    if numtype > 1:
                        if numtype < 17:
                            break
                break
            except:
                cls()
                print('다시 입력해주세요')

        listlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        restlist = []
        quolist = []
        restlist.append('')
        quolist.append(number)
        att = 0

        while True:
            quo = quolist[att] // numtype
            rest = quolist[att] % numtype

            print(str(att) + '. 몫 ' + str(quo))
            print(str(att) + '. 나머지 ' + str(rest))
            print('=' * 10)

            if numtype > 10:
                rest = listlist[rest]

            lastquo = rest

            if quo == 0:
                restlist.append(lastquo)
                break

            quolist.append(quo)
            restlist.append(rest)

            att += 1
            lastquo = quo

            if numtype > 10:
                if lastquo < 16:
                    lastquo = listlist[lastquo]

        print('변환 작업 끝!')
        result = ''
        del restlist[0]
        restlist.reverse()
        print(restlist)


        for x in range(att + 1):
            addresult = restlist[x]
            result = result + str(addresult)
        print('\n')
        print('=' * 20)
        print(str(number) + '(10) -> ' + str(result) + '('+str(numtype)+')')

    elif mode == '2':
        listlist = ['a', 'b', 'c', 'd', 'e', 'f']
        listlist2 = [10, 11, 12, 13, 14, 15]
        while True:
            try:
                number = input('10진수로 변환할 수를 입력하세요>>>')
                numtype = int(input('입력한 수가 몇 진수인지 입력하세요(2~16)>>>'))
                
                temp = number
                if numtype >= 11:
                    temp = temp.replace('a', '')
                    if numtype >= 12:
                        temp = temp.replace('b', '')
                        if numtype >= 13:
                            temp = temp.replace('c', '')
                            if numtype >= 14:
                                temp = temp.replace('d', '')
                                if numtype >= 15:
                                    temp = temp.replace('e', '')
                                    if numtype == 16:
                                        temp = temp.replace('f', '')
                                        temp += '1'
                a = int(temp) + 1
                if numtype > 1:
                    if numtype < 17:
                        break
                
            except:
                #cls()
                print('다시 입력해주세요')

        length = len(number)
        eachpos = []
        for i in range(length):
            eachpos.append('')

        a = 0
        for i in range(length):
            eachpos[a] = number[a:a+1]
            a += 1

        eachpos.reverse()

        a = 0
        for i in range(length):
            temp = eachpos[a]
            temp = temp.replace('a', '10')
            temp = temp.replace('b', '11')
            temp = temp.replace('c', '12')
            temp = temp.replace('d', '13')
            temp = temp.replace('e', '14')
            temp = temp.replace('f', '15')
            eachpos[a] = temp
            a += 1
        

        eachmulti = []
        for i in range(length):
            eachmulti.append('')


        a = 0
        for i in range(length):
            eachmulti[a] = numtype**a
            a += 1

        #TODO

        
        result = []
        for i in range(length):
            result.append('')

        a = 0
        for i in range(length):
            result[a] = int(eachpos[a]) * int(eachmulti[a])
            print(result[a])
            a += 1
        
        fresult = 0
        a = 0
        for i in range(length):
            fresult += int(result[a])
            a += 1

        print('변환 작업 끝!')
        print('='*10)
        print('\n'*2)
        print(str(number) + '('+str(numtype)+') -> ' + str(fresult) + '(10)')

    re = input('\n다른 작업을 다시 하시겠습니까?(y/n)')

    if re == 'n':
        break

    cls()