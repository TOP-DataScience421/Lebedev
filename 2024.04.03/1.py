number1 = float(input())
number2 = float(input())
number3 = float(input())

sum = 0

if number1 > 0:
    sum += number1
if number2 > 0:
    sum += number2
if number3 > 0:
    sum += number3

if sum > 0:
    print(sum)
else:
    print("Положительных нет")
    