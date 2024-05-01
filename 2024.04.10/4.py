digit = int(input())
max_number = "9"
max_number_digit = int(max_number * digit)

total = 0

for n in range(max_number_digit // 10 + 1, max_number_digit + 1):
    for j in range(max_number_digit // 10 + 1, n):
        if n % j == 0:
            break
    else:
        total += n

print(total)

#Не совсем понял суть задания. Понял, что дается разряд и нужно посчитать сумму всех простых чисел в пределах этого разряда. То есть если digit = 3 то считаем сумму всех простых чисел от 100 до 999
