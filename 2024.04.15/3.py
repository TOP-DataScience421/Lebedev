list_1 = [int(num) for num in input().split()]
list_2 = [int(num) for num in input().split()]

len_list_2 = len(list_2)

if any(list_2 == list_1[i: i + len_list_2] for i in range(len(list_1) - len_list_2 + 1)):
    print('Да')
else:
    print('Нет')


#1 2 3 4
#2 5
#Нет

#1 2 3 4
#2 4
#Нет

#1 2 3 4
#3 4
#Да