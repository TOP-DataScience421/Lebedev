user_num = input()
total_first_part = 0
total_second_part = 0

for n in range(3):
    total_first_part += int(user_num[n])
    
for i in range(3, 6):
    total_second_part += int(user_num[i])
    
if total_first_part == total_second_part:
    print("Да")
else:
    print("Нет")
    
#123123
#Да

#156981
#Нет

#696966
#Да

#183534
#Да

#401367
#Нет