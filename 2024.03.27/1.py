import datetime
today = datetime.date.today()
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = int(input('Введите год рождения: '))
print(surname, name, '\b,', today.year - year,)

#Введите имя: Руслан
#Введите фамилию: Лебедев
#Введите год рождения: 1996
#Лебедев Руслан, 28