import datetime
ZNAK=[]
n=2
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


print(ZNAK)
