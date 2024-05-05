user_email = input()

if user_email.count('@') == 1 and user_email[0] != '@' and user_email.find('@') < user_email.find('.'):
    print('Да')
else:
    print('Нет')
    
#dsfsdff@mail.ru
#Да

#dzfsdfsdf@dsfsf
#Нет    