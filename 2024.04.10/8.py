user_num = int(input())

num1 = num2 = 1

print(num1, num2, end = ' ')

for _ in range(2, user_num):
    num1, num2 = num2, num1 + num2
    print(num2, end = ' ')
    
#20
#1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765