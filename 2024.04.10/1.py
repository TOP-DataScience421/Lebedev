numbers = []

user_num = int(input())
while user_num % 7 == 0:
    numbers.append(user_num)
    user_num = int(input())
    
numbers.reverse()

for n in range(len(numbers)):
    print(numbers[n], end=' ')
    
#7
#14
#28
#35
#3
#35 28 14 7