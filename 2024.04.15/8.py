users_input = input()
users_list = users_input.split('; ')

sort_list = sorted(users_list)

new_list = []

for item in sort_list:
    if item not in new_list:
        new_list.append(item)
        count = 2
    else:
        point_index = item.find('.')
        new_item = item[:point_index] + f'_{count}' + item[point_index:]
        new_list.append(new_item)
        count += 1
        
for item in new_list:
    print(item)

#1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.py; 1.py; main.cpp; src.tar.gz
#1.py
#1_2.py
#1_3.py
#aux.h
#functions.h
#main.cpp
#main_2.cpp
#main.py
#src.tar.gz
#src_2.tar.gz