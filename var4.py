import datetime
ZNAK=[]
n=8
print('1) ввод элементов')
for _ in range(n):
    a=[]
    name_fio=input('Введите фамилию и имя: ')
    zodiac=input('Введите знак зодиака: ')
    print('Введите день рождения: ')
    date=[int(input('число: ')),int(input('месяц: ')),int(input('год: '))]
    a.append(name_fio)
    a.append(zodiac)
    a.append(date)
    ZNAK.append(a)

#Сортировка
l=n
for i in range(l):
    for i in range(n-1):
        t1=datetime.date(ZNAK[i][2][2],ZNAK[i][2][1],ZNAK[i][2][0])
        t2=datetime.date(ZNAK[i+1][2][2],ZNAK[i+1][2][1],ZNAK[i+1][2][0])
        if t1 > t2:
            temp=ZNAK[i]
            ZNAK[i]=ZNAK[i+1]
            ZNAK[i + 1]=temp
            l-=1

# Вывод Znak
print('2)Вывод информации')
print(ZNAK)
def RibaLevOutput(ZNK):
    '''
    данная функция выводит сотрудников чьи знаки riba или lev
    '''
    rezult=[]
    for item in ZNK:
        if item[1]=='lev' or item[1]=='riba':
            rezult.append(item[0])

    return rezult
print('3)вывести сотрудников чьи знаки riba или lev')
print(RibaLevOutput(ZNAK))

def HumanInfoOutput(ZNK):
    '''
    данная функция выводит инфу о введённом сотруднике
    '''
    men = input('Введите человека:')
    for item in ZNK:
        if item[0]==men:
            return item
    return None
print('4)вывести информацию о введённом сотруднике')
print(HumanInfoOutput(ZNAK))

def AugustBornCount(ZNK):
    '''
    данная функция выводит количество людей родившихся в августе
    '''
    count = 0
    for item in ZNK:
        if item[2][1] == 8:
            count +=1
    return count
print('5)вывести количество людей родившихся в августе')
print(AugustBornCount(ZNAK))


def Delete30(ZNK):
    '''
        данная функция удаляет из списка людей родившихся 30 числа
        '''
    temp = 0
    for item in ZNK:
        if item[2][0] == 30:
            ZNK.pop(temp)
    temp +=1
    return ZNK

print('6)удалить из списка людей родившихся 30 числа')
print(Delete30(ZNAK))


