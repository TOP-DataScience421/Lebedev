number1 = int(input())
number2 = int(input())

if number1 % number2 == 0:
    print(f'{number1} делится на {number2} нацело \nчастное: {number1 // number2}')
else:
    print(f'{number1} делится на {number2} нацело \nнеполное частное: {number1 // number2}\nостаток: {number1 % number2}')


