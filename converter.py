
def cls():
    from os import system
    system('cls')

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

'''

while True:
    try:
        number = input('10진수로 변환할 수를 입력하세요>>>')
        tester = int(number)
        break
    except:
        cls()
        pass

length = len(number)
eachnum = []
for i in range(length):
    eachnum.append('')
'''