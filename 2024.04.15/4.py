elem_list = []
elem_dict = input()
dict = {}

while elem_dict:
    elem_list.append(elem_dict.split(' '))
    for i, j in elem_list:
        dict[i] = j
    elem_dict = input()    

find_index = input()

for key, value in dict.items():
    if find_index == value:
        print(key)
        break
else:
    print('! value error !')
    
#1004 ER_CANT_CREATE_FILE
#1005 ER_CANT_CREATE_TABLE
#1006 ER_CANT_CREATE_DB
#1007 ER_DB_CREATE_EXISTS
#1010 ER_DB_DROP_RMDIR
#1016 ER_CANT_OPEN_FILE
#1022 ER_DUP_KEY

#ER_CANT_CREATE_DB
#1006

#4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
#4108 ER_GIPK_COLUMN_EXISTS
#4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
#4113 ER_DA_EXPIRE_LOGS_DAYS_IGNORED
#4114 ER_CTE_RECURSIVE_NOT_UNION

#ER_CANT_OPEN_FILE
#! value error !    