def strong_password(user_password: str) -> bool:
    flag = False
    symbols = " /,.:;_\?!|@#$%^&*()-+="
    
    while True:
        if len(user_password) >= 8:
            flag = True
        else:
            return print(False)
            break
    
        if any(char.isupper() for char in user_password) and any(char.islower() for char in user_password):
            flag = True
        else:
            return print(False)
            break
    
        count_digit = 0
    
        for char in user_password:
            if char.isdigit():
                count_digit += 1
                if count_digit >= 2:
                    flag = True
                    break
                else:
                    flag = False
        else:
            return print(False)
            break
                
        for elem in symbols:
            if elem in user_password:
                flag = True
                break
        else:
            return print(False)
            break
        
        if flag:
            return print(True)
            break

#>>> strong_password('Qqwwe19-')
#True
#>>> strong_password('qwe90_')
#False
#>>> strong_password('aP3:kD_l3')
#True
#>>> strong_password('password')
#False



